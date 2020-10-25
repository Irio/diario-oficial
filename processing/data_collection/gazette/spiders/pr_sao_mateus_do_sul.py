from gazette.spiders.instar_base import BaseInstarSpider


class PrSaoMateusdoSUlSpider(BaseInstarSpider):
    TERRITORY_ID = "4125605"
    name = "pr_sao_mateus_do_sul"
    allowed_domains = ["saomateusdosul.pr.gov.br"]
    start_urls = ["https://www.saomateusdosul.pr.gov.br/portal/diario-oficial"]
