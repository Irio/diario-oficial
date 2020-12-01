from datetime import date

from gazette.spiders.base.imprensa_oficial import ImprensaOficialSpider


class BaVeraCruzSpider(ImprensaOficialSpider):

    name = "ba_vera_cruz"
    allowed_domains = ["pmVERACRUZBA.imprensaoficial.org"]
    start_date = date(2017, 4, 1)
    url_base = "http://pmVERACRUZBA.imprensaoficial.org/{}"
    TERRITORY_ID = "2933208"
