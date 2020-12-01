from datetime import date

from gazette.spiders.base.imprensa_oficial import ImprensaOficialSpider


class BaConceicaoDoAlmeidaSpider(ImprensaOficialSpider):

    name = "ba_conceicao_do_almeida"
    allowed_domains = [
        "pmCONCEICAODOALMEIDABA.imprensaoficial.org",
        "conceicaodoalmeida.ba.gov.br",
    ]
    start_date = date(2019, 5, 1)
    url_base = "http://conceicaodoalmeida.ba.gov.br/{}"
    TERRITORY_ID = "2908309"
