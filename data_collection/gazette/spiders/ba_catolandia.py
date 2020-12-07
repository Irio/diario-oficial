from gazette.spiders.base.doem import DoemGazetteSpider


class BaCatolandiaSpider(DoemGazetteSpider):
    TERRITORY_ID = "2907400"
    name = "ba_catolandia"
    state_city_url_part = "ba/catolandia"
