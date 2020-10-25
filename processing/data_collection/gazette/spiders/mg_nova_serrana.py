from gazette.spiders.instar_base import BaseInstarSpider


class MgNovaSerranaSpider(BaseInstarSpider):
    TERRITORY_ID = "3145208"
    name = "mg_nova_serrana"
    allowed_domains = ["novaserrana.mg.gov.br"]
    start_urls = ["https://www.novaserrana.mg.gov.br/portal/diario-oficial/"]
