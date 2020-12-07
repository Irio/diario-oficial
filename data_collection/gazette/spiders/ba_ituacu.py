from gazette.spiders.base.doem import DoemGazetteSpider


class BaItuacuSpider(DoemGazetteSpider):
    TERRITORY_ID = "2917201"
    name = "ba_ituacu"
    state_city_url_part = "ba/ituacu"
