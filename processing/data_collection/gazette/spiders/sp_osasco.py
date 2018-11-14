from datetime import datetime

import dateparser
from scrapy import Request

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class SpOsascoSpider(BaseGazetteSpider):
    TERRITORY_ID = "3534401"

    DATE_CSS = ".document-date span::text"
    GAZETTE_CSS = "ul.document-list li.document"
    NEXT_PAGE_CSS = ".c-pagination li:last-child a::attr(href)"
    URL_CSS = ".document-title a::attr(href)"

    allowed_domains = ["www.osasco.sp.gov.br"]
    name = "sp_osasco"
    start_urls = ["http://www.osasco.sp.gov.br/imprensa-oficial"]

    def parse(self, response):
        """
        @url http://www.osasco.sp.gov.br/imprensa-oficial
        @returns requests 1
        @scrapes date file_urls is_extra_edition territory_id power scraped_at
        """

        for element in response.css(self.GAZETTE_CSS):
            url = element.css(self.URL_CSS).extract_first()
            date = element.css(self.DATE_CSS).extract_first()
            date = dateparser.parse(date, languages=["pt"]).date()

            yield Gazette(
                date=date,
                file_urls=[url],
                is_extra_edition=False,
                territory_id=self.TERRITORY_ID,
                power="executive_legislature",
                scraped_at=datetime.utcnow(),
            )

        for url in response.css(self.NEXT_PAGE_CSS).extract():
            yield Request(url)
