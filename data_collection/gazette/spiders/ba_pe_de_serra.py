from datetime import date

from gazette.spiders.base.imprensa_oficial import ImprensaOficialSpider


class BaPeDeSerraSpider(ImprensaOficialSpider):

    name = "ba_pe_de_serra"
    allowed_domains = ["pmPEDESERRABA.imprensaoficial.org"]
    start_date = date(2017, 1, 1)
    url_base = "http://pmPEDESERRABA.imprensaoficial.org/{}"
    TERRITORY_ID = "2924058"
