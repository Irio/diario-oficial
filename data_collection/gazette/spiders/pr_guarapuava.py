import re
from datetime import date

import scrapy
from dateparser import parse

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class PrGuarapuavaSpider(BaseGazetteSpider):
    TERRITORY_ID = "4109401"
    name = "pr_guarapuava"
    allowed_domains = ["guarapuava.pr.gov.br"]
    start_urls = ["https://www.guarapuava.pr.gov.br/boletins-oficiais"]
    start_date = date(2002, 1, 20)

    def start_requests(self):
        end_date = date.today()
        for year in range(self.start_date.year, end_date.year + 1):
            url = f"https://www.guarapuava.pr.gov.br/boletins-oficiais/{year}-2/"
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for gazette in response.css(".link > a"):
            link = gazette.css("a ::text")
            gazette_date = parse(
                link.re_first(r"(\d+/\d+/\d+)"), languages=["pt"]
            ).date()
            gazette_edition_number = re.search(
                r"Boletim(\s+)Oficial(\s+)(\d+)", link.get()
            ).group(0)
            is_extra_edition = "extra" in link.get().lower()

            if gazette_date is None:
                continue

            yield Gazette(
                date=gazette_date,
                file_urls=[gazette.css("a::attr(href)").get()],
                power="executive",
                edition_number=gazette_edition_number,
                is_extra_edition=is_extra_edition,
            )
