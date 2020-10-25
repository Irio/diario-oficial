from gazette.spiders.instar_base import BaseInstarSpider


class SpAracariguamaSpider(BaseInstarSpider):
    TERRITORY_ID = "3502754"
    name = "sp_aracariguama"
    allowed_domains = ["aracariguama.sp.gov.br"]
    start_urls = ["https://www.aracariguama.sp.gov.br/portal/diario-oficial"]
