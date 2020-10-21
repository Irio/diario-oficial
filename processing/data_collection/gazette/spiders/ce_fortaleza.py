import re
import dateparser
import w3lib.url

from datetime import datetime
from scrapy import Request
from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class CeFortalezaSpider(BaseGazetteSpider):
    GAZETTE_ELEMENT_CSS = ".diarios-oficiais .table-responsive tbody tr"
    DATE_CSS = "td:nth-child(2)::text"
    EXTRA_CSS = "td:nth-child(1)::text"
    NEXT_PAGE_CSS = "ul.pagination .page-link::attr(href)"

    TERRITORY_ID = "2304400"

    allowed_domains = ["apps.fortaleza.ce.gov.br"]
    name = "ce_fortaleza"

    def start_requests(self):
        base_url = "http://apps.fortaleza.ce.gov.br/diariooficial/?mes-diario=todos"

        for year in range(1952, datetime.now().year + 1):
            year_url = w3lib.url.add_or_replace_parameter(base_url, "ano-diario", year)
            yield Request(year_url)

    def parse(self, response):
        for element in response.css(self.GAZETTE_ELEMENT_CSS):
            url = response.urljoin(element.css("a::attr(href)").extract_first())
            date = dateparser.parse(
                element.css(self.DATE_CSS).extract_first(""), languages=["pt"]
            ).date()
            # Extra edition is maked with a "s" on description. Example: Diário Oficial Nº 15923s
            extra_edition = element.css(self.EXTRA_CSS).extract_first("").endswith("s")

            yield Gazette(
                date=date,
                file_urls=[url],
                is_extra_edition=extra_edition,
                power="executive",
            )

        for page_number in response.css(self.NEXT_PAGE_CSS).re("#(\d)+"):
            next_url = w3lib.url.add_or_replace_parameter(
                response.url, "current", page_number
            )
            yield Request(next_url)
