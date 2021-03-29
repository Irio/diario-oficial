from gazette.spiders.base.sigpub import SigpubGazetteSpider


class BaAssociacaoMunicipiosSpider(SigpubGazetteSpider):
    name = "ba_associacao_municipios"
    TERRITORY_ID = "2900000"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/amurc"
    TERRITORIES_COVERAGE = [
        "2900900",
        "2902252",
        "2902401",
        "2903102",
        "2908002",
        "2910909",
        "2912103",
        "2912301",
        "2914901",
        "2916203",
        "2917102",
        "2918555",
        "2920908",
        "2932309",
        "2932705",
    ]
