from gazette.spiders.instar_base import BaseInstarSpider


class SpParisiSpider(BaseInstarSpider):
    TERRITORY_ID = "3536257"
    name = "sp_parisi"
    allowed_domains = ["parisi.sp.gov.br"]
    start_urls = ["https://www.parisi.sp.gov.br/portal/diario-oficial"]
