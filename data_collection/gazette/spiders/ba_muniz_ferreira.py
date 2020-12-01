from datetime import date

from gazette.spiders.base.imprensa_oficial import ImprensaOficialSpider


class BaMunizFerreiraSpider(ImprensaOficialSpider):

    name = "ba_muniz_ferreira"
    allowed_domains = [
        "pmMUNIZFERREIRABA.imprensaoficial.org",
        "munizferreira.ba.gov.br",
    ]
    start_date = date(2014, 12, 1)
    url_base = "http://munizferreira.ba.gov.br/{}"
    TERRITORY_ID = "2922201"
