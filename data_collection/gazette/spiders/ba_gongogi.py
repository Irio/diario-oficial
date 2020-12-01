from datetime import date

from gazette.spiders.base.imprensa_oficial import ImprensaOficialSpider


class BaGongogiSpider(ImprensaOficialSpider):

    name = "ba_gongogi"
    allowed_domains = ["pmGONGOGIBA.imprensaoficial.org", "gongogi.ba.gov.br"]
    start_date = date(2020, 2, 1)
    url_base = "http://gongogi.ba.gov.br/{}"
    TERRITORY_ID = "2911501"
