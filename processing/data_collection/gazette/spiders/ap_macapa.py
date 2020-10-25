import datetime as dt

import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class ApMacapaSpider(BaseGazetteSpider):

    name = "ap_macapa"
    allowed_domains = ["macapa.ap.gov.br"]
    start_date = None

    TERRITORY_ID = "1600303"

    def __init__(self, start_date=None, end_date=None, *args, **kwargs):
        self.start_date = dt.date(2018, 1, 1)
        self.end_date = dt.date.today()

        super(ApMacapaSpider, self).__init__(start_date, end_date)

        self.logger.debug(
            "Start date is {date}".format(date=self.start_date.isoformat())
        )
        self.logger.debug("End date is {date}".format(date=self.end_date.isoformat()))

    def start_requests(self):
        base_url = "https://macapa.ap.gov.br/"

        target_date = self.start_date
        data = {
            "s": "",
            "post_type": "official_diaries",
            "search": "official_diaries",
            "official_diary_number": "",
        }
        while target_date <= self.end_date:
            formatted_date = target_date.strftime("%d/%m/%Y")
            data.update(
                {
                    "official_diary_initial_date": formatted_date,
                    "official_diary_final_date": formatted_date,
                }
            )

            yield scrapy.FormRequest(
                url=base_url, formdata=data, method="GET", meta={"date": target_date}
            )
            target_date = target_date + dt.timedelta(days=1)

    def parse(self, response):
        # Extract Items
        links = response.xpath('//i[@class="fa fa-file-pdf-o"]/parent::a')
        links = links.xpath("@href").getall()

        gazette_date = response.meta["date"]

        if len(links) == 0:
            self.logger.warning(
                "No gazettes found for date {date}".format(date=gazette_date)
            )

        for index, file_url in enumerate(links):
            yield Gazette(
                date=gazette_date,
                file_urls=[file_url],
                is_extra_edition=(index > 0),
                territory_id=self.TERRITORY_ID,
                power="executive_legislative",
                scraped_at=dt.datetime.utcnow(),
            )
