from gazette.spiders.instar_base import BaseInstarSpider


class MgSalinasSpider(BaseInstarSpider):
    TERRITORY_ID = "3157005"
    name = "mg_salinas"
    allowed_domains = ["salinas.mg.gov.br"]
    start_urls = ["https://www.salinas.mg.gov.br/portal/diario-oficial"]
