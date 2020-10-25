from gazette.spiders.base import SigpubGazetteSpider


class GoAssociacaoMunicipiosSpider(SigpubGazetteSpider):
    name = "go_associacao_municipios_fgm"
    TERRITORY_ID = "5200000"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/fgm"
