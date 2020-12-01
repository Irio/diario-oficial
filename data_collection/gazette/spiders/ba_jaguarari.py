from datetime import date

from gazette.spiders.base.imprensa_oficial import ImprensaOficialSpider


class BaJaguarariSpider(ImprensaOficialSpider):

    name = "ba_jaguarari"
    allowed_domains = ["pmJAGUARARIBA.imprensaoficial.org"]
    start_date = date(2019, 10, 1)
    url_base = "http://pmJAGUARARIBA.imprensaoficial.org/{}"
    TERRITORY_ID = "2917706"
