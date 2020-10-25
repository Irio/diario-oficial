from gazette.spiders.base import SigpubGazetteSpider


class RnAssociacaoMunicipiosSpider(SigpubGazetteSpider):
    name = "rn_associacao_municipios"
    TERRITORY_ID = "2400000"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/femurn"
