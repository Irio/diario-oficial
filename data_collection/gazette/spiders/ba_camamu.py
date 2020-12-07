from gazette.spiders.base.doem import DoemGazetteSpider


class BaCamamuSpider(DoemGazetteSpider):
    TERRITORY_ID = "2905800"
    name = "ba_camamu"
    state_city_url_part = "ba/camamu"
