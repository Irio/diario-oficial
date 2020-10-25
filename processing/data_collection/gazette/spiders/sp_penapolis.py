from gazette.spiders.instar_base import BaseInstarSpider


class SpPenapolis(BaseInstarSpider):
    TERRITORY_ID = "3537305"
    name = "sp_penapolis"
    allowed_domains = ["penapolis.sp.gov.br"]
    start_urls = ["https://www.penapolis.sp.gov.br/portal/diario-oficial"]
