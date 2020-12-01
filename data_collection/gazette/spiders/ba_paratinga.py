from datetime import date

from gazette.spiders.base.imprensa_oficial import ImprensaOficialSpider


class BaParatingaSpider(ImprensaOficialSpider):

    name = "ba_paratinga"
    allowed_domains = ["pmPARATINGABA.imprensaoficial.org"]
    start_date = date(2018, 4, 1)
    url_base = "http://pmPARATINGABA.imprensaoficial.org/{}"
    TERRITORY_ID = "2923704"
