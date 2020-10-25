from gazette.spiders.instar_base import BaseInstarSpider


class SpPrataniaSpider(BaseInstarSpider):
    TERRITORY_ID = "3541059"
    name = "sp_pratania"
    allowed_domains = ["pratania.sp.gov.br"]
    start_urls = ["https://www.pratania.sp.gov.br/portal/diario-oficial"]
