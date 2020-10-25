from gazette.spiders.instar_base import BaseInstarSpider


class RsCerritoSpider(BaseInstarSpider):
    TERRITORY_ID = "4305124"
    name = "rs_cerrito"
    allowed_domains = ["cerrito.rs.gov.br"]
    start_urls = ["https://www.cerrito.rs.gov.br/portal/diario-oficial"]
