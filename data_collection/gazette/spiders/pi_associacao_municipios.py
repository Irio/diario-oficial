from gazette.spiders.base.sigpub import SigpubGazetteSpider


class PiAssociacaoMunicipiosSpider(SigpubGazetteSpider):
    name = "pi_associacao_municipios"
    TERRITORY_ID = "2200000"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/appm"
    TERRITORIES_COVERAGE = [
        "2200202",
        "2200459",
        "2201150",
        "2201176",
        "2201408",
        "2201705",
        "2201929",
        "2201945",
        "2202778",
        "2202851",
        "2203305",
        "2203354",
        "2203800",
        "2204501",
        "2205003",
        "2205102",
        "2205458",
        "2205524",
        "2205599",
        "2205607",
        "2206407",
        "2206696",
        "2207850",
        "2208106",
        "2208601",
        "2209005",
        "2209500",
        "2210003",
        "2210623",
        "2210805",
        "2210904",
        "2211605",
    ]
