from gazette.spiders.base.doem import DoemGazetteSpider


class BaIpiauSpider(DoemGazetteSpider):
    TERRITORY_ID = "2913903"
    name = "ba_ipiau"
    state_city_url_part = "ba/ipiau"
