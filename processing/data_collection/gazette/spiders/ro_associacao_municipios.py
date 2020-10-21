from gazette.spiders.base import SigpubGazetteSpider


class RoAssociacaoMunicipiosSpider(SigpubGazetteSpider):
    name = "ro_associacao_municipios"
    TERRITORY_ID = "1100000"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/arom"
