from gazette.spiders.instar_base import BaseInstarSpider


class SpBaraodeAntoninaSpider(BaseInstarSpider):
    TERRITORY_ID = "3505005"
    name = "sp_barao_de_antonina"
    allowed_domains = ["baraodeantonina.sp.gov.br"]
    start_urls = ["https://www.baraodeantonina.sp.gov.br/portal/diario-oficial"]
