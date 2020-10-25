from gazette.spiders.instar_base import BaseInstarSpider


class MgCandeiasSpider(BaseInstarSpider):
    TERRITORY_ID = "3112000"
    name = "mg_candeias"
    allowed_domains = ["candeias.mg.gov.br"]
    start_urls = ["https://www.candeias.mg.gov.br/portal/diario-oficial"]
