from gazette.spiders.base.doem import DoemGazetteSpider


class BaSenhorDoBonfimSpider(DoemGazetteSpider):
    TERRITORY_ID = "2930105"
    name = "ba_senhor_do_bonfim"
    state_city_url_part = "ba/senhordobonfim"
