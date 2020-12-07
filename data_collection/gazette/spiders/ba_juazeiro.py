from gazette.spiders.base.doem import DoemGazetteSpider


class BaJuazeiroSpider(DoemGazetteSpider):
    TERRITORY_ID = "2918407"
    name = "ba_juazeiro"
    state_city_url_part = "ba/juazeiro"
