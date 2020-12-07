from gazette.spiders.base.doem import DoemGazetteSpider


class BaMedeirosNetoSpider(DoemGazetteSpider):
    TERRITORY_ID = "2921104"
    name = "ba_medeiros_neto"
    state_city_url_part = "ba/medeirosneto"
