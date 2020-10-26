import base64
from datetime import datetime

import chompjs
import dateparser
from scrapy import Request, Spider

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class SpItuSpider(BaseGazetteSpider):
    TERRITORY_ID = "3523909"
    PDF_URL = "https://dosp.com.br/exibe_do.php?i={}"

    GAZETTE_API_URL = "https://www.dosp.com.br/api/index.php/dioe.js/4923"

    allowed_domains = ["dosp.com.br"]
    name = "sp_itu"

    def start_requests(self):
        yield Request(self.GAZETTE_API_URL)

    def parse(self, response):

        response_js = chompjs.parse_js_object(response.text)

        for element in response_js.get("data"):
            date = self.extract_date(element)
            url = self.extract_url(element)
            edition_number = self.extract_edition_number(element)
            is_extra_edition = self.extract_is_extra_edition(element)

            yield Gazette(
                date=date,
                file_urls=[url],
                edition_number=edition_number,
                is_extra_edition=is_extra_edition,
                power="executive_legislature",
            )

    def extract_date(self, element):
        journal_date = element.get("data")
        parse_date = dateparser.parse(
            date_string=journal_date, date_formats=["%Y-%m-%d"], languages=["pt"]
        ).date()
        return parse_date

    def extract_edition_number(self, element):
        return element.get("edicao_do")

    def extract_is_extra_edition(self, element):
        return bool(element.get("flag_extra"))

    def extract_url(self, element):
        iddo = str(element.get("iddo")).encode("ascii")
        pdf_id = base64.b64encode(iddo).decode("ascii")
        return self.PDF_URL.format(pdf_id)
