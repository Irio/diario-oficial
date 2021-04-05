from gazette.spiders.base.sigpub import SigpubGazetteSpider


class SpAssociacaoMunicipiosSpider(SigpubGazetteSpider):
    name = "sp_associacao_municipios"
    TERRITORY_ID = "3500000"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/apm"
    TERRITORIES_COVERAGE = [
        "3505401",
        "3506805",
        "3521507",
        "3523909",
        "3524006",
        "3530508",
        "3553807",
    ]
