import datetime
import re
from urllib.parse import urlencode

import dateparser
import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class BaCamacari(BaseGazetteSpider):
    TERRITORY_ID = "2905701"
    BASE_URL = "http://www.camacari.ba.gov.br/wp-content/themes/camacari/assets/ajax/arquivos.php"
    name = "ba_camacari"
    allowed_domains = ["camacari.ba.gov.br"]
    start_date = datetime.date(2007, 10, 10)

    def start_requests(self):
        params = {"paged": 1, "categoria": "diario-oficial"}
        url = f"{self.BASE_URL}?{urlencode(params)}"
        yield scrapy.Request(url=url, meta={"params": params})

    def parse(self, response):
        document_list = response.css(".col-sm-12")
        last_scraped_gazette_date = datetime.date.today()

        for document in document_list:
            date_text = document.css(".mb-10::text").re_first(r"\d+\/\d+\/\d+")
            date = datetime.datetime.strptime(date_text, "%d/%m/%Y").date()

            file_url = document.css("a::attr(href)").get()

            title = document.css("a::text").get()
            edition_number = re.search(r"\d+", title.replace(".", "")).group(0)
            is_extra_edition = bool(re.search(r"EXTRA", title, re.IGNORECASE))

            yield Gazette(
                date=date,
                file_urls=[file_url],
                is_extra_edition=is_extra_edition,
                territory_id=self.TERRITORY_ID,
                power="executive",
                scraped_at=datetime.datetime.utcnow(),
                edition_number=edition_number,
            )

            last_scraped_gazette_date = date

        if document_list and self.start_date <= last_scraped_gazette_date:
            next_params = response.meta["params"]
            next_params["paged"] += 1
            next_url = f"{self.BASE_URL}?{urlencode(next_params)}"
            yield scrapy.Request(url=next_url, meta={"params": next_params})
