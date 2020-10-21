from gazette.spiders.base import SigpubGazetteSpider


class MgAssociacaoMunicipiosSpider(SigpubGazetteSpider):
    name = "mg_associacao_municipios"
    TERRITORY_ID = "3100000"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/amm-mg"
