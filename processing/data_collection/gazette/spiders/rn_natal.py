from datetime import date, datetime

import dateparser
from dateutil.rrule import rrule, MONTHLY
from scrapy import FormRequest

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class RnNatalSpider(BaseGazetteSpider):

    name = "rn_natal"
    allowed_domains = ["www.natal.rn.gov.br"]
    start_date = date(2003, 1, 1)

    TERRITORY_ID = "2408102"

    def start_requests(self):
        base_url = "http://www.natal.rn.gov.br/dom/"

        initial_date = date(self.start_date.year, self.start_date.month, 1)
        end_date = date.today()

        periods_of_interest = [
            (date.year, date.month)
            for date in rrule(freq=MONTHLY, dtstart=initial_date, until=end_date)
        ]
        for year, month in periods_of_interest:
            data = {"ano": str(year), "mes": str(month).zfill(2), "list": "Listar"}
            yield FormRequest(url=base_url, formdata=data)

    def parse(self, response):
        for entry in response.css("#texto a"):
            file_url = response.urljoin(entry.css("::attr(href)").get())
            title = entry.css("::text").get()
            date = dateparser.parse(title.split("-")[-1], languages=["pt"]).date()
            extra_edition = "Extra" in title

            yield Gazette(
                date=date,
                file_urls=[file_url],
                is_extra_edition=extra_edition,
                territory_id=self.TERRITORY_ID,
                power="executive_legislative",
                scraped_at=datetime.utcnow(),
            )
