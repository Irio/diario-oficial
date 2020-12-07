from gazette.spiders.base.doem import DoemGazetteSpider


class BaCanudosSpider(DoemGazetteSpider):
    TERRITORY_ID = "2906824"
    name = "ba_canudos"
    state_city_url_part = "ba/canudos"
