from gazette.spiders.instar_base import BaseInstarSpider


class RsCamaquaSpider(BaseInstarSpider):
    TERRITORY_ID = "4303509"
    name = "rs_camaqua"
    allowed_domains = ["camaqua.rs.gov.br"]
    start_urls = ["https://www.camaqua.rs.gov.br/portal/diario-oficial"]
