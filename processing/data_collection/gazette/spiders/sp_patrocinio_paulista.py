from gazette.spiders.instar_base import BaseInstarSpider


class SpPatrocinioPaulistaSpider(BaseInstarSpider):
    TERRITORY_ID = "3536307"
    name = "sp_patrocinio_paulista"
    allowed_domains = ["patrociniopaulista.sp.gov.br"]
    start_urls = ["https://www.patrociniopaulista.sp.gov.br/portal/diario-oficial"]
