from gazette.spiders.base.sigpub import SigpubGazetteSpider


class RjAssociacaoMunicipiosSpider(SigpubGazetteSpider):
    name = "rj_associacao_municipios"
    TERRITORY_ID = "3300000"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/aemerj"
    TERRITORIES_COVERAGE = [
        "3300159",
        "3300225",
        "3300605",
        "3301603",
        "3301801",
        "3302809",
        "3302858",
        "3303955",
        "3306107",
        "3306206",
    ]
