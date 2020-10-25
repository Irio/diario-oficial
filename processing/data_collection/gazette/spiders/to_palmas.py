import datetime
from urllib.parse import urlencode

import dateparser
import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class ToPalmasSpider(BaseGazetteSpider):
    TERRITORY_ID = "1721000"
    name = "to_palmas"
    allowed_domains = ["diariooficial.palmas.to.gov.br"]
    start_date = datetime.date(2010, 3, 22)  # First gazette available

    custom_settings = {
        "MEDIA_ALLOW_REDIRECTS": True,
    }

    def start_requests(self):
        dt_inicial = self.start_date.strftime("%d/%m/%Y")
        dt_final = datetime.date.today().strftime("%d/%m/%Y")

        url_params = {
            "opcao": "datas",
            "dt_inicial": dt_inicial,
            "dt_final": dt_final,
            "btn_search": "Search",
        }
        params = urlencode(url_params)
        url = f"http://diariooficial.palmas.to.gov.br/resultado-pesquisa/?{params}"
        yield scrapy.Request(url)

    def _get_date_from_parent_edition(self, response, gazette):
        parent_gazette_class_id = gazette.re_first(r"treegrid-parent-(\d+)")
        parent_gazette_class = f"treegrid-{parent_gazette_class_id}"
        main_edition_gazette = response.css(f".{parent_gazette_class}")
        return main_edition_gazette.xpath("./td[2]/text()").get()

    def parse(self, response):
        gazettes = response.css(".diario-resultado-pesquisa tbody tr")
        for gazette in gazettes:
            gazette_date = gazette.xpath("./td[2]/text()").get()
            gazette_url = response.urljoin(gazette.css("a::attr(href)").get())

            is_extra_edition = bool(gazette.xpath(".//*[contains(., 'Suplemento')]"))
            if is_extra_edition:
                # Extra Editions doesn't have a date in its line. We need to get it from
                # the main edition of that day
                gazette_date = self._get_date_from_parent_edition(response, gazette)

            item = Gazette(
                date=dateparser.parse(gazette_date, languages=["pt"]).date(),
                is_extra_edition=is_extra_edition,
                territory_id=self.TERRITORY_ID,
                scraped_at=datetime.datetime.utcnow(),
                power="executive_legislative",
            )
            yield scrapy.Request(
                gazette_url,
                method="HEAD",
                callback=self.parse_pdf_url,
                cb_kwargs={"item": item},
            )

        next_pages_urls = response.css(".pagination a::attr(href)").getall()
        for next_page_url in next_pages_urls:
            yield scrapy.Request(response.urljoin(next_page_url))

    def parse_pdf_url(self, response, item):
        gazette_pdf_url = response.url
        item = Gazette(**item)
        item["file_urls"] = [gazette_pdf_url]
        yield item
