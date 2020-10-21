from gazette.spiders.base import SigpubGazetteSpider
from gazette.spiders.instar_base import BaseInstarSpider


class SpMonteAltoSpider(BaseInstarSpider):
    TERRITORY_ID = "3531308"
    name = "sp_monte_alto"
    allowed_domains = ["montealto.instaridc.com.br"]
    start_urls = ["http://montealto.instaridc.com.br/portal/diario-oficial"]


class SpMonteAltoSigpubSpider(SigpubGazetteSpider):
    name = "sp_monte_alto_sigpub"
    TERRITORY_ID = "3531308"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/pmmasp"
