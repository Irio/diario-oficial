from gazette.spiders.instar_base import BaseInstarSpider


class RjArraialdoCabopider(BaseInstarSpider):
    TERRITORY_ID = "3300258"
    name = "rj_arraial_do_cabo"
    allowed_domains = ["rraial.rj.gov.br/"]
    start_urls = ["https://www.arraial.rj.gov.br/portal/diario-oficial"]
