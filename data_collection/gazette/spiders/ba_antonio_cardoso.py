from gazette.spiders.base.doem import DoemGazetteSpider


class BaAntonioCardosoSpider(DoemGazetteSpider):
    TERRITORY_ID = "2901700"
    name = "ba_antonio_cardoso"
    state_city_url_part = "ba/antoniocardoso"
