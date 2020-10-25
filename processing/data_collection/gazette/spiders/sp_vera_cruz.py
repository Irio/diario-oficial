from gazette.spiders.instar_base import BaseInstarSpider


class SpVeraCruzSpider(BaseInstarSpider):
    TERRITORY_ID = "3556602"
    name = "sp_vera_cruz"
    allowed_domains = ["veracruz.sp.gov.br"]
    start_urls = ["https://www.veracruz.sp.gov.br/portal/diario-oficial"]
