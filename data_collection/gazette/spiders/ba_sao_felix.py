from datetime import date

from gazette.spiders.base.imprensa_oficial import ImprensaOficialSpider


class BaSaoFelixSpider(ImprensaOficialSpider):

    name = "ba_sao_felix"
    allowed_domains = ["pmSAOFELIXBA.imprensaoficial.org"]
    start_date = date(2017, 1, 1)
    url_base = "http://pmSAOFELIXBA.imprensaoficial.org/{}"
    TERRITORY_ID = "2929008"
