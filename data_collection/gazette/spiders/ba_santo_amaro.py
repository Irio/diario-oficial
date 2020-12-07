from gazette.spiders.base.doem import DoemGazetteSpider


class BaSantoAmaroSpider(DoemGazetteSpider):
    TERRITORY_ID = "2928604"
    name = "ba_santo_amaro"
    state_city_url_part = "ba/santoamaro"
