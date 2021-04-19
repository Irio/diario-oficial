from gazette.spiders.base.instar import BaseInstarSpider


class RjSaoGoncaloSpider(BaseInstarSpider):

    TERRITORY_ID = "3304904"
    name = "rj_sao_goncalo"
    allowed_domains = ["www.saogoncalo.rj.gov.br"]
    start_urls = ["https://servicos.pmsg.rj.gov.br/diario_oficial"]
