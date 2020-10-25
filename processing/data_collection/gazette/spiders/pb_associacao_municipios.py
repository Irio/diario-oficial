from gazette.spiders.base import SigpubGazetteSpider


class PbAssociacaoMunicipiosSpider(SigpubGazetteSpider):
    name = "pb_associacao_municipios"
    TERRITORY_ID = "2500000"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/famup"
