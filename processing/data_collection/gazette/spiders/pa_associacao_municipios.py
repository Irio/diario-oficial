from gazette.spiders.base import SigpubGazetteSpider


class PaAssociacaoMunicipiosSpider(SigpubGazetteSpider):
    name = "pa_associacao_municipios"
    TERRITORY_ID = "1500000"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/famep"
