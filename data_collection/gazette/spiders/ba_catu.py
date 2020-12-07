from gazette.spiders.base.doem import DoemGazetteSpider


class BaCatuSpider(DoemGazetteSpider):
    TERRITORY_ID = "2907509"
    name = "ba_catu"
    state_city_url_part = "ba/catu"
