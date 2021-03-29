from gazette.spiders.base.sigpub import SigpubGazetteSpider


class MsAssociacaoMunicipiosSpider(SigpubGazetteSpider):
    name = "ms_associacao_municipios"
    TERRITORY_ID = "5000000"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/ms"
    TERRITORIES_COVERAGE = [
        "5000203",
        "5000609",
        "5000708",
        "5000856",
        "5000906",
        "5001003",
        "5001102",
        "5001508",
        "5001904",
        "5002001",
        "5002100",
        "5002159",
        "5002209",
        "5002308",
        "5002605",
        "5002803",
        "5002902",
        "5003157",
        "5003306",
        "5003454",
        "5003488",
        "5003504",
        "5003751",
        "5003801",
        "5003900",
        "5004106",
        "5004304",
        "5004403",
        "5004809",
        "5004908",
        "5005004",
        "5005103",
        "5005152",
        "5005202",
        "5005251",
        "5005400",
        "5005608",
        "5005707",
        "5006200",
        "5006309",
        "5006358",
        "5006408",
        "5006606",
        "5006903",
        "5007109",
        "5007307",
        "5007505",
        "5007695",
        "5007802",
        "5007703",
        "5007901",
        "5007935",
        "5007976",
        "5008008",
        "5008305",
        "5008404",
    ]
