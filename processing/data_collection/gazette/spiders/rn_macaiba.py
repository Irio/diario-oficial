import datetime as dt
import re

import dateparser
import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class RnMacaiba(BaseGazetteSpider):

    TERRITORY_ID = "2407104"
    name = "rn_macaiba"
    allowed_domains = ["macaiba.rn.gov.br"]

    def __init__(self, start_date=None, end_date=None):
        self.start_date = dt.date(2010, 5, 14)
        self.end_date = dt.date.today()

        super(RnMacaiba, self).__init__(start_date, end_date)

        self.logger.debug(
            "Start date is {date}".format(date=self.start_date.isoformat())
        )
        self.logger.debug("End date is {date}".format(date=self.end_date.isoformat()))

    def start_requests(self):
        yield scrapy.FormRequest(
            "https://www.macaiba.rn.gov.br/boletins/busca",
            method="POST",
            formdata={
                "inicio": self.start_date.isoformat(),
                "fim": self.end_date.isoformat(),
            },
        )

    def parse(self, response):
        for item in response.css("div.conteudo li.collection-item div"):
            gazette = item.css("::text").get().strip()
            date_match = re.findall(
                r"(\d{2}) ([a-zç]+), (\d{4})", gazette, re.IGNORECASE
            )
            if len(date_match) != 1:
                self.logger.error(f"Could not parse the date for Gazette {gazette}")
                continue

            item_date = " de ".join(date_match.pop())
            item_date = dateparser.parse(item_date, languages=["pt"]).date()
            file_url = item.css("a::attr(href)").get().lower()

            if not file_url.endswith("pdf"):
                self.logger.warning(
                    f"Broken URL found for Gazette {gazette} - {file_url}"
                )
                continue

            yield Gazette(
                date=item_date,
                file_urls=[file_url],
                is_extra_edition=False,
                territory_id=self.TERRITORY_ID,
                power="executive_legislature",
                scraped_at=dt.datetime.utcnow(),
            )
