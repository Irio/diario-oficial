from gazette.spiders.base import SigpubGazetteSpider


class PiAssociacaoMunicipiosSpider(SigpubGazetteSpider):
    name = "pi_associacao_municipios"
    TERRITORY_ID = "2200000"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/appm"
