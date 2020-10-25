from gazette.spiders.instar_base import BaseInstarSpider


class SpSarutaiaSpider(BaseInstarSpider):
    TERRITORY_ID = "3551207"
    name = "sp_sarutaia"
    allowed_domains = ["sarutaia.sp.gov.br"]
    start_urls = ["https://www.sarutaia.sp.gov.br/portal/diario-oficial"]
