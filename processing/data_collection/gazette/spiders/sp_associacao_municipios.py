from gazette.spiders.base import SigpubGazetteSpider


class SpAssociacaoMunicipiosSpider(SigpubGazetteSpider):
    name = "sp_associacao_municipios"
    TERRITORY_ID = "3500000"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/apm"
