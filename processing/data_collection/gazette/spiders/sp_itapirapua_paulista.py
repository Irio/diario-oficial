from gazette.spiders.instar_base import BaseInstarSpider


class SpItapirapuaPaulistaSpider(BaseInstarSpider):
    TERRITORY_ID = "3522653"
    name = "sp_itapirapua_paulista"
    allowed_domains = ["itapirapuapaulista.sp.gov.br"]
    start_urls = ["https://www.itapirapuapaulista.sp.gov.br/portal/diario-oficial"]
