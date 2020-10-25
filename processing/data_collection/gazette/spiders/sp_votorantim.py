from gazette.spiders.instar_base import BaseInstarSpider


class SpVotorantimSpider(BaseInstarSpider):
    TERRITORY_ID = "3557006"
    name = "sp_votorantim"
    allowed_domains = ["votorantim.sp.gov.br"]
    start_urls = ["https://www.votorantim.sp.gov.br/portal/diario-oficial"]
