from gazette.spiders.base.doem import DoemGazetteSpider


class BaAlcobacaSpider(DoemGazetteSpider):
    TERRITORY_ID = "2900801"
    name = "ba_alcobaca"
    state_city_url_part = "ba/alcobaca"
