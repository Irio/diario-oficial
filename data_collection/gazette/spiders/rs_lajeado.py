from datetime import date
from urllib.parse import urlencode

import dateparser
from scrapy import Request

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class RsLajeadoSpider(BaseGazetteSpider):
    TERRITORY_ID = "4311403"
    BASE_URL = "https://lajeado.rs.gov.br/"

    name = "rs_lajeado"
    start_date = date(2016, 4, 5)
    params = {
        "titulo": "Diário Oficial",
        "template": "conteudo",
        "codigoCategoria": 1012,
    }

    def start_requests(self):
        params = urlencode(self.params)
        yield Request(f"{self.BASE_URL}?{params}")

    def parse(self, response):
        pdfs = response.css("ul.anexos li a")
        for item in pdfs:
            filename = item.css("::text").get()

            kwargs = {
                "gazette_date": self.extract_date(filename),
                "edition_number": self.extract_edition(filename),
            }

            href = response.urljoin(item.attrib["href"])
            yield Request(href, callback=self.parse_url, cb_kwargs=kwargs)

    def parse_url(self, response, gazette_date=None, edition_number=None):
        url = response.css("div.topoAbreAnexoDownload a::attr(href)").get()
        yield Gazette(
            date=gazette_date,
            edition_number=edition_number,
            file_urls=[url],
            power="executive",
            territory_id=self.TERRITORY_ID,
        )

    def extract_date(self, filename):
        filedate, *_ = filename.split("_")

        # There is a single case where the first day
        # of the month is represented like '1º'
        filedate = filedate.replace("º", "")
        filedate = dateparser.parse(filedate, languages=["pt"])
        return filedate.date()

    def extract_edition(self, filename):
        return filename.lower().split("_edição_")[1].split()[0]
