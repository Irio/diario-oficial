from datetime import date

from gazette.spiders.base.imprensa_oficial import ImprensaOficialSpider


class BaAmeliaRodriguesSpider(ImprensaOficialSpider):

    name = "ba_amelia_rodrigues"
    allowed_domains = ["pmameliarodriguesba.imprensaoficial.org"]
    start_date = date(2015, 1, 1)
    url_base = "http://pmameliarodriguesba.imprensaoficial.org/{}"
    TERRITORY_ID = "2930501"
