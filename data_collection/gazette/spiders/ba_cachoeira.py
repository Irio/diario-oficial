from gazette.spiders.base.doem import DoemGazetteSpider


class BaCachoeiraSpider(DoemGazetteSpider):
    TERRITORY_ID = "2904902"
    name = "ba_cachoeira"
    state_city_url_part = "ba/cachoeira"
