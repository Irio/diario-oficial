from gazette.spiders.instar_base import BaseInstarSpider


class MsMaracajuSpider(BaseInstarSpider):
    TERRITORY_ID = "5005400"
    name = "ms_maracaju"
    allowed_domains = ["maracaju.ms.gov.br"]
    start_urls = ["https://www.maracaju.ms.gov.br/portal/diario-oficial"]
