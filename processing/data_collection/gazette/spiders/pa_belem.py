import json

import requests
import scrapy
from dateparser import parse

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class PaBelemSpider(BaseGazetteSpider):
    TERRITORY_ID = "1501402"
    name = "pa_belem"
    allowed_domains = ["sistemas.belem.pa.gov.br"]
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8,application/octet-stream"
        }
    }

    BASE_URL = "https://sistemas.belem.pa.gov.br/diario-consulta-api/diarios"

    def start_requests(self):
        """
        Requests the gazette to get the total of documents and use it as a query param

        @url https://sistemas.belem.pa.gov.br/diario-consulta-api/diarios
        @returns requests 1
        """

        gazettes_data = requests.get(self.BASE_URL).json()
        number_of_documents = gazettes_data["response"]["numFound"]

        url = f"{self.BASE_URL}?start=0&rows={number_of_documents}"

        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        @url https://sistemas.belem.pa.gov.br/diario-consulta-api/diarios?start=0&rows={x]
        @returns requests 1
        @scrapes date file_urls is_extra_edition power
        """

        data = json.loads(response.body)["response"]

        for gazette_data in data["docs"]:
            date = parse(gazette_data["data_publicacao"]).date()
            gazette_id = gazette_data["id"]

            url = f"{self.BASE_URL}/{gazette_id}"

            yield Gazette(
                date=date,
                file_urls=[url],
                is_extra_edition=bool(None),
                power="executive",
            )
