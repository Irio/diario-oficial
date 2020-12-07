from gazette.spiders.base.doem import DoemGazetteSpider


class BaTabocasDoBrejoVelhoSpider(DoemGazetteSpider):
    TERRITORY_ID = "2930907"
    name = "ba_tabocas_do_brejo_velho"
    state_city_url_part = "ba/tabocasdobrejovelho"
