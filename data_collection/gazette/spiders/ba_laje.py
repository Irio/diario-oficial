from gazette.spiders.base.doem import DoemGazetteSpider


class BaLajeSpider(DoemGazetteSpider):
    TERRITORY_ID = "2918902"
    name = "ba_laje"
    state_city_url_part = "ba/laje"
