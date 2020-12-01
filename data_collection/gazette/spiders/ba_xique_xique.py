from datetime import date

from gazette.spiders.base.imprensa_oficial import ImprensaOficialSpider


class BaXiqueXiqueSpider(ImprensaOficialSpider):

    name = "ba_xique_xique"
    allowed_domains = ["pmXIQUEXIQUEBA.imprensaoficial.org"]
    start_date = date(2017, 1, 1)
    url_base = "http://pmXIQUEXIQUEBA.imprensaoficial.org/{}"
    TERRITORY_ID = "2933604"
