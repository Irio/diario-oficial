from gazette.spiders.base import SigpubGazetteSpider


class GoAssociacaoMunicipiosSpider(SigpubGazetteSpider):
    name = "go_associacao_municipios_agm"
    TERRITORY_ID = "5200000"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/agm"
