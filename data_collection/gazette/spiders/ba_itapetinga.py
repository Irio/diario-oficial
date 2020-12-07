from gazette.spiders.base.doem import DoemGazetteSpider


class BaItapetingaSpider(DoemGazetteSpider):
    TERRITORY_ID = "2916401"
    name = "ba_itapetinga"
    state_city_url_part = "ba/itapetinga"
