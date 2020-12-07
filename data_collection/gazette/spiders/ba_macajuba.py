from gazette.spiders.base.doem import DoemGazetteSpider


class BaMacajubaSpider(DoemGazetteSpider):
    TERRITORY_ID = "2919603"
    name = "ba_macajuba"
    state_city_url_part = "ba/macajuba"
