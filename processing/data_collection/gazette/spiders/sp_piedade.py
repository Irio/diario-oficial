from gazette.spiders.instar_base import BaseInstarSpider


class SpPiedadeSpider(BaseInstarSpider):
    TERRITORY_ID = "3537800"
    name = "sp_piedade"
    allowed_domains = ["piedade.sp.gov.br"]
    start_urls = ["https://www.piedade.sp.gov.br/portal/diario-oficial"]
