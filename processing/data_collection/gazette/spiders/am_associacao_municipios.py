from gazette.spiders.base import SigpubGazetteSpider


class AmAssociacaoMunicipiosSpider(SigpubGazetteSpider):
    name = "am_associacao_municipios"
    TERRITORY_ID = "1300000"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/aam"
