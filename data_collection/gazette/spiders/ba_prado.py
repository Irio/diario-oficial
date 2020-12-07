from gazette.spiders.base.doem import DoemGazetteSpider


class BaPradoSpider(DoemGazetteSpider):
    TERRITORY_ID = "2925501"
    name = "ba_prado"
    state_city_url_part = "ba/prado"
