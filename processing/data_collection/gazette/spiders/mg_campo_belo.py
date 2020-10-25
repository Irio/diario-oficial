from gazette.spiders.instar_base import BaseInstarSpider


class MgCampoBeloSpider(BaseInstarSpider):
    TERRITORY_ID = "3111200"
    name = "mg_campo_belo"
    allowed_domains = ["campobelo.mg.gov.br"]
    start_urls = ["https://www.campobelo.mg.gov.br/portal/diario-oficial"]
