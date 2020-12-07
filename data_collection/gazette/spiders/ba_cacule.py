from gazette.spiders.base.doem import DoemGazetteSpider


class BaCaculeSpider(DoemGazetteSpider):
    TERRITORY_ID = "2905008"
    name = "ba_cacule"
    state_city_url_part = "ba/cacule"
