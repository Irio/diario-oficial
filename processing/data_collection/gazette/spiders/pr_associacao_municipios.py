from gazette.spiders.base import SigpubGazetteSpider


class PrAssociacaoMunicipiosSpider(SigpubGazetteSpider):
    name = "pr_associacao_municipios"
    TERRITORY_ID = "4100000"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/amp"
