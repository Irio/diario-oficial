import re
from datetime import datetime

from scrapy import Request

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class SpPresidentePrudenteSpider(BaseGazetteSpider):
    TERRITORY_ID = "3541406"
    GAZETTE_URL = "https://www.gdoe.com.br/presidenteprudente/1"
    allowed_domains = ["gdoe.com.br"]
    name = "sp_presidente_prudente"

    def start_requests(self):
        yield Request(self.GAZETTE_URL, callback=self.parse)

    def parse(self, response):
        for doc in response.xpath('//div[@class="col-md-4"]/a'):
            yield self.parse_gazette(doc)

        next_page = (
            response.xpath('//ul[@class="pagination"]/li')[-1]
            .css("a::attr(href)")
            .get()
        )

        if "javascript:void(0)" not in next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_gazette(self, response):
        doc_url = response.css("a::attr(href)").get()
        doc_date = self.get_date(response.css("a::text")[1].get())

        if doc_date is None:
            return None

        return Gazette(
            date=doc_date,
            file_urls=(doc_url,),
            is_extra_edition=False,
            territory_id=self.TERRITORY_ID,
            scraped_at=datetime.utcnow(),
            power="executive",
        )

    @staticmethod
    def get_date(text):
        pattern = r"\d+\/\d+\/\d+"
        match = re.search(pattern, text)
        if not match:
            return None

        return match.group()
