from gazette.spiders.base import SigpubGazetteSpider


class CeAssociacaoMunicipiosSpider(SigpubGazetteSpider):
    name = "ce_associacao_municipios"
    TERRITORY_ID = "2300000"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/aprece"
