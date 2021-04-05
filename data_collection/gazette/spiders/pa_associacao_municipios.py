from gazette.spiders.base.sigpub import SigpubGazetteSpider


class PaAssociacaoMunicipiosSpider(SigpubGazetteSpider):
    name = "pa_associacao_municipios"
    TERRITORY_ID = "1500000"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/famep"
    TERRITORIES_COVERAGE = [
        "1500107",
        "1500131",
        "1500347",
        "1500859",
        "1500958",
        "1501303",
        "1501451",
        "1501576",
        "1501600",
        "1501709",
        "1501725",
        "1501782",
        "1501808",
        "1501907",
        "1502103",
        "1502152",
        "1502202",
        "1502509",
        "1502608",
        "1502707",
        "1502764",
        "1502772",
        "1502855",
        "1502939",
        "1503200",
        "1503408",
        "1503457",
        "1503507",
        "1503606",
        "1503705",
        "1503754",
        "1503903",
        "1504059",
        "1504109",
        "1504208",
        "1504422",
        "1504455",
        "1504703",
        "1504752",
        "1504802",
        "1504901",
        "1504976",
        "1505007",
        "1505031",
        "1505064",
        "1505106",
        "1505304",
        "1505437",
        "1505486",
        "1505494",
        "1505502",
        "1505601",
        "1505635",
        "1505650",
        "1505809",
        "1505908",
        "1506005",
        "1506138",
        "1506161",
        "1506187",
        "1506195",
        "1506203",
        "1506302",
        "1506559",
        "1506807",
        "1506906",
        "1507102",
        "1507151",
        "1507300",
        "1507409",
        "1507458",
        "1507474",
        "1507508",
        "1507607",
        "1507755",
        "1507805",
        "1507904",
        "1508001",
        "1508035",
        "1508050",
        "1508084",
        "1508100",
        "1508308",
        "1508407",
    ]
