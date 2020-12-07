from gazette.spiders.base.doem import DoemGazetteSpider


class BaIraraSpider(DoemGazetteSpider):
    TERRITORY_ID = "2914505"
    name = "ba_irara"
    state_city_url_part = "ba/irara"
