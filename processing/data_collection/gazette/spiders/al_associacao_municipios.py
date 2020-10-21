from gazette.spiders.base import SigpubGazetteSpider


class AlAssociacaoMunicipiosSpider(SigpubGazetteSpider):
    name = "al_associacao_municipios"
    TERRITORY_ID = "2700000"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/ama"
