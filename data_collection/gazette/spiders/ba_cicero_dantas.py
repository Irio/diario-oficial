from gazette.spiders.base.doem import DoemGazetteSpider


class BaCiceroDantasSpider(DoemGazetteSpider):
    TERRITORY_ID = "2907806"
    name = "ba_cicero_dantas"
    state_city_url_part = "ba/cicerodantas"
