from gazette.spiders.base.doem import DoemGazetteSpider


class BaFlorestaAzulSpider(DoemGazetteSpider):
    TERRITORY_ID = "2911006"
    name = "ba_floresta_azul"
    state_city_url_part = "ba/florestaazul"
