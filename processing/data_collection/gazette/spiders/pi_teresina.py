import math
from datetime import datetime
from urllib.parse import urlencode

import dateparser
import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class PiTeresina(BaseGazetteSpider):
    TERRITORY_ID = "2211001"
    BASE_URL = "http://dom.pmt.pi.gov.br/lista_diario.php"
    name = "pi_teresina"
    allowed_domains = ["dom.pmt.pi.gov.br"]
    start_urls = [BASE_URL]

    def parse(self, response):
        total_items = int(response.css(".texto span b::text").get())
        ITEMS_PER_PAGE = 10
        total_pages = math.ceil(total_items / ITEMS_PER_PAGE)

        for i in range(1, total_pages + 1):
            params = {"pagina": i}
            url = f"{self.BASE_URL}?{urlencode(params)}"
            yield scrapy.Request(url=url, callback=self.parse_page)

    def parse_page(self, response):
        for entry in response.css("tbody tr"):
            # retrieves gazette files and attachments
            file_urls = entry.css("td a::attr(href)").getall()

            date_text = entry.css("td:nth-child(2)::text").get()
            date = dateparser.parse(date_text, languages=["pt"]).date()

            yield Gazette(
                date=date,
                file_urls=file_urls,
                territory_id=self.TERRITORY_ID,
                power="executive_legislative",
                scraped_at=datetime.utcnow(),
            )
