from gazette.spiders.base import SigpubGazetteSpider


class RjAssociacaoMunicipiosSpider(SigpubGazetteSpider):
    name = "rj_associacao_municipios"
    TERRITORY_ID = "3300000"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/aemerj"
