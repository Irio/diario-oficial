from datetime import date

from gazette.spiders.base.imprensa_oficial import ImprensaOficialSpider


class BaSaoFelipeSpider(ImprensaOficialSpider):

    name = "ba_sao_felipe"
    allowed_domains = ["pmSAOFELIPEBA.imprensaoficial.org", "saofelipe.ba.gov.br"]
    start_date = date(2020, 1, 1)
    url_base = "http://saofelipe.ba.gov.br/{}"
    TERRITORY_ID = "2929107"
