from datetime import date

from gazette.spiders.base.imprensa_oficial import ImprensaOficialSpider


class BaSaoFranciscoDoCondeSpider(ImprensaOficialSpider):

    name = "ba_sao_francisco_do_conde"
    allowed_domains = ["pmSAOFRANCISCODOCONDEBA.imprensaoficial.org"]
    start_date = date(2019, 3, 1)
    url_base = "http://pmSAOFRANCISCODOCONDEBA.imprensaoficial.org/{}"
    TERRITORY_ID = "2929206"
