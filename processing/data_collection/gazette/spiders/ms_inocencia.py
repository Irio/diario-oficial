from gazette.spiders.instar_base import BaseInstarSpider


class MsInocenciaSpider(BaseInstarSpider):
    TERRITORY_ID = "5004403"
    name = "ms_inocencia"
    allowed_domains = ["inocencia.ms.gov.br"]
    start_urls = ["https://www.inocencia.ms.gov.br/portal/diario-oficial"]
