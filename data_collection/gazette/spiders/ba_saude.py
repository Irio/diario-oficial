from datetime import date

from gazette.spiders.base.imprensa_oficial import ImprensaOficialSpider


class BaSaudeSpider(ImprensaOficialSpider):

    name = "ba_saude"
    allowed_domains = ["pmSAUDEBA.imprensaoficial.org"]
    start_date = date(2018, 2, 1)
    url_base = "http://pmSAUDEBA.imprensaoficial.org/{}"
    TERRITORY_ID = "2929800"
