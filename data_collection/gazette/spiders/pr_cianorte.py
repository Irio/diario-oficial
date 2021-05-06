from dateparser import parse
from scrapy.http import Request

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class PrCianorteSpider(BaseGazetteSpider):
    TERRITORY_ID = "4105508"
    name = "pr_cianorte"
    allowed_domains = ["cianorte.pr.gov.br"]
    start_urls = ["https://cianorte.pr.gov.br/orgao-oficial/"]
    current_page = 1
    base_url = "https://cianorte.pr.gov.br/orgao-oficial/pagina/"

    def parse(self, response):
        lines = response.css("tr")[1:]
        if len(lines):
            for row in lines:
                date = row.xpath("td[2]/text()").extract()[0]
                edition_number = row.xpath("td[1]/text()").extract()[0]

                yield Gazette(
                    date=parse(date, languages=["pt"]).date(),
                    edition_number=edition_number,
                    file_urls=[row.css("a::attr(href)").get()],
                    is_extra_edition=False,
                    power="executive_legislative",
                )
                self.current_page += 1
                yield Request(self.base_url + str(self.current_page))
