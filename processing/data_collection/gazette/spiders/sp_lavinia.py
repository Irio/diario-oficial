from gazette.spiders.instar_base import BaseInstarSpider


class SpLaviniaSpider(BaseInstarSpider):
    TERRITORY_ID = "3526506"
    name = "sp_lavinia"
    allowed_domains = ["lavinia.sp.gov.br"]
    start_urls = ["https://www.lavinia.sp.gov.br/portal/diario-oficial"]
