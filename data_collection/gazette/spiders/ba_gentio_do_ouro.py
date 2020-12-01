from datetime import date

from gazette.spiders.base.imprensa_oficial import ImprensaOficialSpider


class BaGentioDoOuroSpider(ImprensaOficialSpider):

    name = "ba_gentio_do_ouro"
    allowed_domains = ["pmGENTIODOOUROBA.imprensaoficial.org"]
    start_date = date(2017, 2, 1)
    url_base = "http://pmGENTIODOOUROBA.imprensaoficial.org/{}"
    TERRITORY_ID = "2911303"
