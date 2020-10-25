from gazette.spiders.instar_base import BaseInstarSpider


class MgCarmodaCachoeiraSpider(BaseInstarSpider):
    TERRITORY_ID = "3113909"
    name = "mg_carmo_da_cachoeira"
    allowed_domains = ["carmodacachoeira.mg.gov.br"]
    start_urls = ["https://www.carmodacachoeira.mg.gov.br/portal/diario-oficial"]
