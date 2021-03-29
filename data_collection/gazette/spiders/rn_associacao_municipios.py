from gazette.spiders.base.sigpub import SigpubGazetteSpider


class RnAssociacaoMunicipiosSpider(SigpubGazetteSpider):
    name = "rn_associacao_municipios"
    TERRITORY_ID = "2400000"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/femurn"
    TERRITORIES_COVERAGE = [
        "2400109",
        "2400307",
        "2400406",
        "2400505",
        "2400604",
        "2400802",
        "2400901",
        "2401008",
        "2401107",
        "2401404",
        "2401453",
        "2401503",
        "2401602",
        "2401651",
        "2401701",
        "2401800",
        "2401859",
        "2401909",
        "2402006",
        "2402105",
        "2402204",
        "2402303",
        "2402402",
        "2402600",
        "2402709",
        "2402808",
        "2402907",
        "2403004",
        "2403103",
        "2403202",
        "2403301",
        "2403400",
        "2403509",
        "2403608",
        "2403707",
        "2403756",
        "2403905",
        "2404002",
        "2404101",
        "2404200",
        "2404309",
        "2404408",
        "2404507",
        "2404606",
        "2404705",
        "2404804",
        "2404853",
        "2404903",
        "2405009",
        "2405108",
        "2405207",
        "2405405",
        "2405504",
        "2405603",
        "2405702",
        "2405801",
        "2405900",
        "2406007",
        "2406106",
        "2406155",
        "2406205",
        "2406304",
        "2406403",
        "2406502",
        "2406601",
        "2406700",
        "2406809",
        "2406908",
        "2407005",
        "2407252",
        "2407302",
        "2407401",
        "2407500",
        "2407609",
        "2407708",
        "2407807",
        "2407906",
        "2408003",
        "2408201",
        "2408300",
        "2408409",
        "2408508",
        "2408607",
        "2408706",
        "2408805",
        "2408904",
        "2409209",
        "2409308",
        "2409506",
        "2409605",
        "2409704",
        "2409803",
        "2409902",
        "2410009",
        "2410108",
        "2410207",
        "2410405",
        "2410504",
        "2410603",
        "2410702",
        "2410801",
        "2410900",
        "2408953",
        "2411007",
        "2411106",
        "2411205",
        "2409332",
        "2411403",
        "2411429",
        "2411502",
        "2411601",
        "2411700",
        "2411809",
        "2411908",
        "2412104",
        "2412203",
        "2412302",
        "2412401",
        "2412500",
        "2412559",
        "2412609",
        "2412708",
        "2412906",
        "2413003",
        "2413102",
        "2413201",
        "2410306",
        "2413300",
        "2413359",
        "2413409",
        "2413508",
        "2413557",
        "2413607",
        "2413706",
        "2413904",
        "2414001",
        "2414100",
        "2414159",
        "2411056",
        "2414209",
        "2414308",
        "2414407",
        "2414456",
        "2414506",
        "2414605",
        "2414704",
        "2414753",
        "2414803",
        "2414902",
        "2415008",
        "2403806",
        "2400208",
        "2401206",
        "2405306",
    ]
