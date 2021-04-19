import datetime

import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class SpSaoJoseDoRioPreto(BaseGazetteSpider):
    TERRITORY_ID = "3549805"
    name = "sp_sao_jose_do_rio_preto"
    allowed_domains = ["riopreto.sp.gov.br"]

    base_url = "https://www.riopreto.sp.gov.br/DiarioOficial/Diario!"
    day_url = base_url + "listar.action?diario.dataPublicacao={}/{}/{}"
    doc_url = base_url + "arquivo.action?diario.codPublicacao={}"

    start_date = datetime.date(2006, 5, 3)
    end_date = datetime.date.today()
    custom_settings = {"USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0"}

    def start_requests(self):
        date = self.start_date
        while date <= self.end_date:
            url = self.day_url.format(date.day, date.month, date.year)
            yield scrapy.Request(url=url, cb_kwargs={"gazette_date": date})
            date += datetime.timedelta(days=1)

    def parse(self, response, gazette_date):
        doc_ids = response.css("a").re("codPublicacao=(\d+)")
        for doc_id in doc_ids:
            gazette_url = self.doc_url.format(doc_id)
            yield Gazette(date=gazette_date, file_urls=[gazette_url], power="executive")
