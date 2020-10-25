from gazette.spiders.instar_base import BaseInstarSpider


class MgPiranguinhoSpider(BaseInstarSpider):
    TERRITORY_ID = "3151008"
    name = "mg_piranguinho"
    allowed_domains = ["piranguinho.mg.gov.br"]
    start_urls = ["https://www.piranguinho.mg.gov.br/portal/diario-oficial"]
