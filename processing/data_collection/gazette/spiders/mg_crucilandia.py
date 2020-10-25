from gazette.spiders.instar_base import BaseInstarSpider


class MgCrucilandiaSpider(BaseInstarSpider):
    TERRITORY_ID = "3120607"
    name = "mg_crucilandia"
    allowed_domains = ["prefeituradecrucilandia.mg.gov.br"]
    start_urls = ["http://www.prefeituradecrucilandia.mg.gov.br/portal/diario-oficial"]
