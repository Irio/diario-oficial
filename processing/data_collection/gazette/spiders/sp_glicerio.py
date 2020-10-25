from gazette.spiders.instar_base import BaseInstarSpider


class SpGlicerioSpider(BaseInstarSpider):
    TERRITORY_ID = "3517109"
    name = "sp_glicerio"
    allowed_domains = ["glicerio.sp.gov.br"]
    start_urls = ["https://www.glicerio.sp.gov.br/portal/diario-oficial/"]
