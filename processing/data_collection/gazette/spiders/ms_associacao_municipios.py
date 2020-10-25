from gazette.spiders.base import SigpubGazetteSpider


class MsAssociacaoMunicipiosSpider(SigpubGazetteSpider):
    name = "ms_associacao_municipios"
    TERRITORY_ID = "5000000"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/ms"
