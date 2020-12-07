from gazette.spiders.base.doem import DoemGazetteSpider


class BaRibeiraDoPombalSpider(DoemGazetteSpider):
    TERRITORY_ID = "2926608"
    name = "ba_ribeira_do_pombal"
    state_city_url_part = "ba/ribeiradopombal"
