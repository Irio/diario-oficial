from gazette.spiders.instar_base import BaseInstarSpider


class SpIbitingaSpider(BaseInstarSpider):
    TERRITORY_ID = "3519600"
    name = "sp_ibitinga"
    allowed_domains = ["ibitinga.instarbr.com.br"]
    start_urls = ["https://www.ibitinga.instarbr.com.br/portal/diario-oficial/"]
