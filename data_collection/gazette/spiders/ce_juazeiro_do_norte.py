import datetime as dt
import re

import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class CeJuazeiroDoNorteSpider(BaseGazetteSpider):
    TERRITORY_ID = "2307304"
    name = "ce_juazeiro_do_norte"
    allowed_domains = ["juazeiro.ce.gov.br"]
    start_date = dt.date(year=2009, month=1, day=1)
    end_date = dt.date.today()
    base_url = "https://juazeiro.ce.gov.br"

    def start_requests(self):
        """
        Creates requests for each date since `start_date`.

        The system allows requests for a date range (from beginning-date to end-date)
        or for a single date. This spider uses the single date method.
        """
        target_date = self.start_date
        while target_date <= self.end_date:
            formatted_date = target_date.strftime("%d-%m-%Y")
            search_url = f"{self.base_url}/Imprensa/Diario-Oficial/{formatted_date}/"

            yield scrapy.Request(
                url=search_url,
                meta={"date": target_date},
            )
            target_date = target_date + dt.timedelta(days=1)

    def parse(self, response):
        links = set(
            [element.attrib["href"] for element in response.css("section.diario a")]
        )
        file_urls = [f"{self.base_url}/{link}" for link in links]
        gazette_date = response.meta["date"]

        if len(links) > 0:
            edition = re.findall(r"/Num(.+?)-", file_urls[0])[0]

            yield Gazette(
                date=gazette_date,
                file_urls=file_urls,
                edition_number=edition,
                power="executive_legislative",
            )
