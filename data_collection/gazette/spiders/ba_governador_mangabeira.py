from datetime import date

from gazette.spiders.base.imprensa_oficial import ImprensaOficialSpider


class BaGovernadorMangabeiraSpider(ImprensaOficialSpider):

    name = "ba_governador_mangabeira"
    allowed_domains = ["pmGOVERNADORMANGABEIRABA.imprensaoficial.org"]
    start_date = date(2018, 1, 1)
    url_base = "http://pmGOVERNADORMANGABEIRABA.imprensaoficial.org/{}"
    TERRITORY_ID = "2911600"
