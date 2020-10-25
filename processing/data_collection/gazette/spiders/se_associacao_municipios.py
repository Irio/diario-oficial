from gazette.spiders.base import SigpubGazetteSpider


class SeAssociacaoMunicipiosSpider(SigpubGazetteSpider):
    name = "se_associacao_municipios"
    TERRITORY_ID = "2800000"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/sergipe"
