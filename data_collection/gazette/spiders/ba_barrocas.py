from gazette.spiders.base.doem import DoemGazetteSpider


class BaBarrocasSpider(DoemGazetteSpider):
    TERRITORY_ID = "2903276"
    name = "ba_barrocas"
    state_city_url_part = "ba/barrocas"
