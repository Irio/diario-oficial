from dateparser import parse
from datetime import datetime

import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class SpGuaruja(BaseGazetteSpider):
    TERRITORY_ID = "3518701"
    name = "sp_guaruja"
    allowed_domains = ["guaruja.sp.gov.br"]
    start_urls = ["http://www.guaruja.sp.gov.br/index.php/diario-oficial/"]

    def parse(self, response):
        months = response.css("div.span12 a::attr(href)").extract()
        for month_url in months:
            yield scrapy.Request(month_url, self.parse_items)

    def parse_items(self, response):
        gazettes = response.css("div.span12 p")
        for gazette in gazettes:
            date = gazette.css("a ::text").extract_first()
            is_extra_edition = "parte" in date and "parte1" not in date
            extra_editions = [is_extra_edition, True]
            date = parse(date, languages=["pt"]).date()
            urls = gazette.css("a::attr(href)").extract()
            for url, is_extra_edition in zip(urls, extra_editions):
                yield Gazette(
                    date=date,
                    file_urls=[url],
                    is_extra_edition=is_extra_edition,
                    territory_id=self.TERRITORY_ID,
                    power="executive_legislature",
                    scraped_at=datetime.utcnow(),
                )
