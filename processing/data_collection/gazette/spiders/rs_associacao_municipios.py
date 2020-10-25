from gazette.spiders.base import SigpubGazetteSpider


class RsAssociacaoMunicipiosSpider(SigpubGazetteSpider):
    name = "rs_associacao_municipios"
    TERRITORY_ID = "4300000"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/famurs"
