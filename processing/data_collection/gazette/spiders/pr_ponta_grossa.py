from dateparser import parse
from datetime import date
import re

import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class PrPontaGrossaSpider(BaseGazetteSpider):
    TERRITORY_ID = "4119905"
    name = "pr_ponta_grossa"
    allowed_domains = ["pontagrossa.pr.gov.br"]
    start_urls = ["http://www.pontagrossa.pr.gov.br/diario-oficial/"]
    starting_year = 2015

    def parse(self, response):
        links = response.css(".view-content .field a")
        smallest_year = min(
            (p["date"].year for p in self.pdf_infos(links, self.starting_year)),
            default=0,
        )
        if smallest_year >= self.starting_year:
            next_page_url = response.urljoin(
                response.css(".pager-next a::attr(href)").extract_first()
            )
            yield scrapy.Request(next_page_url)
            for pdf_info in self.pdf_infos(links, self.starting_year):
                gazette_date = pdf_info["date"].strftime("%Y-%m-%d")
                yield Gazette(
                    date=gazette_date,
                    file_urls=[pdf_info["url"]],
                    is_extra_edition=pdf_info["is_extra_edition"],
                    power="executive_legislature",
                )

    @staticmethod
    def pdf_infos(links, starting_year):
        link_pattern = ".*/diario-oficial/_?(\d{4})-(\d{2})-(\d{2}).*.pdf"
        for link in links:
            file_name = link.css("::attr(href)").extract_first()
            link_text = link.css("::text").extract_first()
            if "sem_atos" in file_name:
                continue
            info = re.search(link_pattern, file_name)
            year = int(info.group(1))
            if year < starting_year:
                continue

            month, day = int(info.group(2)), int(info.group(3))
            yield {
                "date": date(year, month, day),
                "is_extra_edition": "complementar" in link_text,
                "url": file_name,
            }
