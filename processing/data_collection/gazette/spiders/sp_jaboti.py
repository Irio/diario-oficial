from gazette.spiders.instar_base import BaseInstarSpider


class PrJabotiSpider(BaseInstarSpider):
    TERRITORY_ID = "4111704"
    name = "pr_jaboti"
    allowed_domains = ["jaboti.pr.gov.br"]
    start_urls = ["https://www.jaboti.pr.gov.br/portal/diario-oficial"]
