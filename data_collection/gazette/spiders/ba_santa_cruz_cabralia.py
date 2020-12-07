from gazette.spiders.base.doem import DoemGazetteSpider


class BaSantaCruzCabraliaSpider(DoemGazetteSpider):
    TERRITORY_ID = "2927705"
    name = "ba_santa_cruz_cabralia"
    state_city_url_part = "ba/santacruzcabralia"
