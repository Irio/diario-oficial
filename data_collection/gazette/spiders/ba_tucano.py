from gazette.spiders.base.doem import DoemGazetteSpider


class BaTucanoSpider(DoemGazetteSpider):
    TERRITORY_ID = "2931905"
    name = "ba_tucano"
    state_city_url_part = "ba/tucano"
