from gazette.spiders.base import SigpubGazetteSpider


class RrAssociacaoMunicipiosSpider(SigpubGazetteSpider):
    name = "rr_associacao_municipios"
    TERRITORY_ID = "1400000"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/amr"
