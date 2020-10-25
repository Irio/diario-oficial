from datetime import datetime

import scrapy
from dateparser import parse

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class AlMaceioSpider(BaseGazetteSpider):
    TERRITORY_ID = "2704302"

    name = "al_maceio"
    allowed_domains = ["maceio.al.gov.br"]
    start_urls = ["http://www.maceio.al.gov.br/noticias/diario-oficial/"]

    def parse(self, response):
        gazettes = response.xpath("//article")
        for gazette in gazettes:
            url = gazette.xpath("a/@href").get()
            if not url:  # In some cases the href attr is empty, e.g. 24-11-2015
                continue

            gazette_date = gazette.xpath("time/text()").get()
            date = parse(gazette_date, languages=["pt"]).date()

            title = gazette.xpath("a/@title").get()
            is_extra_edition = "suplemento" in title.lower()

            if "wp-content/uploads" in url:
                gazette = self.create_gazette(date, url, is_extra_edition)
                yield gazette
            else:
                yield scrapy.Request(
                    url,
                    callback=self.parse_additional_page,
                    meta={"date": date, "is_extra_edition": is_extra_edition,},
                )

        next_pages = response.css(".envolve-content nav a::attr(href)").getall()
        for next_page_url in next_pages:
            yield scrapy.Request(next_page_url)

    def parse_additional_page(self, response):
        url = response.css("p.attachment a::attr(href)").get()
        gazette = self.create_gazette(
            response.meta["date"], url, response.meta["is_extra_edition"]
        )
        yield gazette

    def create_gazette(self, date, url, is_extra_edition):
        return Gazette(
            date=date,
            file_urls=[url],
            is_extra_edition=is_extra_edition,
            territory_id=self.TERRITORY_ID,
            power="executive_legislature",
            scraped_at=datetime.utcnow(),
        )
