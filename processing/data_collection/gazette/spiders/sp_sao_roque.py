from gazette.spiders.instar_base import BaseInstarSpider


class SpSaoRoqueSpider(BaseInstarSpider):
    TERRITORY_ID = "3550605"
    name = "sp_sao_roque"
    allowed_domains = ["saoroque.sp.gov.br"]
    start_urls = ["https://www.saoroque.sp.gov.br/portal/diario-oficial"]
