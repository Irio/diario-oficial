from gazette.spiders.base.doem import DoemGazetteSpider


class PePetrolinaSpider(DoemGazetteSpider):
    TERRITORY_ID = "2611101"
    name = "pe_petrolina"
    state_city_url_part = "pe/petrolina"
