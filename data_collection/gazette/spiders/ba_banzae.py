from gazette.spiders.base.doem import DoemGazetteSpider


class BaBanzaeSpider(DoemGazetteSpider):
    TERRITORY_ID = "2902658"
    name = "ba_banzae"
    state_city_url_part = "ba/banzae"
