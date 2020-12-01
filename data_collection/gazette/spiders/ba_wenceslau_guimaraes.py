from datetime import date

from gazette.spiders.base.imprensa_oficial import ImprensaOficialSpider


class BaWenceslauGuimaraesSpider(ImprensaOficialSpider):

    name = "ba_wenceslau_guimaraes"
    allowed_domains = ["pmWENCESLAUGUIMARAESBA.imprensaoficial.org"]
    start_date = date(2017, 1, 1)
    url_base = "http://pmWENCESLAUGUIMARAESBA.imprensaoficial.org/{}"
    TERRITORY_ID = "2933505"
