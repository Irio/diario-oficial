from dateparser import parse
import datetime as dt

import scrapy
from scrapy.http import Request

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class RsCaxiasDoSulSpider(BaseGazetteSpider):
    TERRITORY_ID = "4305108"
    name = "rs_caxias_do_sul"
    allowed_domains = ["caxias.rs.gov.br"]
    start_urls = [
        (
            "https://doe.caxias.rs.gov.br/site/index"
            "?PublicacoesSearch[dt_publicacao]="
            "&PublicacoesSearch[dt_range]=01-01-15+até+31-12-{}"
            "&PublicacoesSearch[palavra_chave]="
            "&PublicacoesSearch[num_publicacao]="
            "&page=1"
        )
    ]

    def start_requests(self):
        current_year = dt.date.today().strftime("%y")
        url = self.start_urls[0].format(current_year)
        yield scrapy.Request(url)

    def parse(self, response):
        for gazette_node in response.css(".table tbody tr"):
            item = self.gazette(response, gazette_node)
            pdf_page_url = gazette_node.css("a::attr(href)").extract_first()
            pdf_page_url = response.urljoin(pdf_page_url)
            gazette_request = Request(pdf_page_url, callback=self.parse_pdf_page)
            gazette_request.meta["item"] = item
            yield gazette_request

        css_path = ".pagination .next a::attr(href)"
        next_page_url = response.css(css_path).extract_first()
        next_page_url = response.urljoin(next_page_url)
        if next_page_url:
            yield Request(next_page_url)

    def gazette(self, response, gazette_node):
        cells = gazette_node.css("td::text")
        date = parse(cells[1].extract(), languages=["pt"]).date()
        is_extra_edition = cells[2].extract() != "Normal"
        return Gazette(
            date=date, is_extra_edition=is_extra_edition, power="executive_legislature",
        )

    def parse_pdf_page(self, response):
        item = response.meta["item"]
        item["file_urls"] = [
            response.css('[type="application/pdf"]::attr(data)').extract_first()
        ]
        return item
