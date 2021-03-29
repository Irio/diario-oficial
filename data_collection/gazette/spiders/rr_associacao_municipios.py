from gazette.spiders.base.sigpub import SigpubGazetteSpider


class RrAssociacaoMunicipiosSpider(SigpubGazetteSpider):
    name = "rr_associacao_municipios"
    TERRITORY_ID = "1400000"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/amr"
    TERRITORIES_COVERAGE = [
        "1400050",
        "1400100",
        "1400407",
        "1400472",
        "1400704",
        "1400027",
        "1400159",
        "1400209",
        "1400233",
        "1400282",
        "1400308",
        "1400506",
        "1400605",
        "1400175",
    ]
