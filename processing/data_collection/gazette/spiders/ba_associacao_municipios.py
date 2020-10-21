from gazette.spiders.base import SigpubGazetteSpider


class BaAssociacaoMunicipiosSpider(SigpubGazetteSpider):
    name = "ba_associacao_municipios"
    TERRITORY_ID = "2900000"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/amurc"
