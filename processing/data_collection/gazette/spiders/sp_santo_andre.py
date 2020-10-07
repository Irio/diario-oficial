import dateparser
from datetime import datetime

from scrapy_splash import SplashRequest

from gazette.settings import USER_AGENT
from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class SpSantoAndreSpider(BaseGazetteSpider):
    name = "sp_santo_andre"
    allowed_domains = ["santoandre.sp.gov.br"]
    start_urls = [
        "http://www.santoandre.sp.gov.br/publicacao/edicao/consultaedicao.aspx"
    ]

    def start_requests(self):
        for url in self.start_urls:
            request = SplashRequest(
                url, self.parse, args={"wait": 0.8}, headers={"User-Agent": USER_AGENT}
            )
            yield request

    def parse(self, response):
        import pdb

        pdb.set_trace()
