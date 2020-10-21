import json

import scrapy
from dateparser import parse

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class GoAparecidaDeGoianiaSpider(BaseGazetteSpider):
    TERRITORY_ID = "5201405"
    name = "go_aparecida_de_goiania"
    allowed_domains = ["aparecida.go.gov.br"]
    start_urls = ["https://webio.aparecida.go.gov.br/api/diof/lista"]

    def parse(self, response):
        download_url = "https://webio.aparecida.go.gov.br/diariooficial/download/{}"

        records = json.loads(response.text)["records"]
        for record in records:
            url = download_url.format(record["numero"])
            power = "executive_legislature"
            date = parse(record["publicado"], languages=["en"]).date()

            yield Gazette(
                date=date, file_urls=[url], is_extra_edition=False, power=power,
            )
