from gazette.spiders.base.sigpub import SigpubGazetteSpider


class SeAssociacaoMunicipiosSpider(SigpubGazetteSpider):
    name = "se_associacao_municipios"
    TERRITORY_ID = "2800000"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/sergipe"
    TERRITORIES_COVERAGE = [
        "2802809",
        "2804300",
        "2805505",
        "2806206",
        "2807105",
        "2807402",
        "2801009",
        "2805000",
        "2805109",
        "2805208",
        "2806305",
    ]
