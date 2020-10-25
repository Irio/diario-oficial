from gazette.spiders.instar_base import BaseInstarSpider


class RsVeracruzSpider(BaseInstarSpider):
    TERRITORY_ID = "4322707"
    name = "rs_vera_cruz"
    allowed_domains = ["veracruz.rs.gov.br"]
    start_urls = ["https://www.veracruz.rs.gov.br/portal/diario-oficial"]
