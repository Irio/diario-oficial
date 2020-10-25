from gazette.spiders.base import SigpubGazetteSpider


class SpMacatubaSpider(SigpubGazetteSpider):
    name = "sp_macatuba"
    TERRITORY_ID = "3528007"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/macatuba"
