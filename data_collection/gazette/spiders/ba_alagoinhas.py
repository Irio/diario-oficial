from gazette.spiders.base.doem import DoemGazetteSpider


class BaAlagoinhasSpider(DoemGazetteSpider):
    TERRITORY_ID = "2900702"
    name = "ba_alagoinhas"
    state_city_url_part = "ba/alagoinhas"
