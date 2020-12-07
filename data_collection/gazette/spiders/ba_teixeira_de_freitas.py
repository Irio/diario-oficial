from gazette.spiders.base.doem import DoemGazetteSpider


class BaTeixeiraDeFreitasSpider(DoemGazetteSpider):
    TERRITORY_ID = "2931350"
    name = "ba_teixeira_de_freitas"
    state_city_url_part = "ba/teixeiradefreitas"
