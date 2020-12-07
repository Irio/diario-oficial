from gazette.spiders.base.doem import DoemGazetteSpider


class BaBrotasDeMacaubasSpider(DoemGazetteSpider):
    TERRITORY_ID = "2904506"
    name = "ba_brotas_de_macaubas"
    state_city_url_part = "ba/brotasdemacaubas"
