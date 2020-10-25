from gazette.spiders.instar_base import BaseInstarSpider


class MgItaunaSpider(BaseInstarSpider):
    TERRITORY_ID = "3133808"
    name = "mg_itauna"
    allowed_domains = ["itauna.mg.gov.br"]
    start_urls = ["https://www.itauna.mg.gov.br/portal/diario-oficial/"]
