import re
from datetime import date
from math import ceil

import dateparser
from scrapy import Request

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class CeSobralSpider(BaseGazetteSpider):
    name = "ce_sobral"
    TERRITORY_ID = "2312908"
    start_urls = ["http://www.sobral.ce.gov.br/diario/pesquisa"]
    start_date = date(2017, 2, 6)
    end_date = date.today()

    def parse(self, response):
        total_gazettes = response.xpath("//div[@class = 'right']/text()").get()
        total_pages = ceil(int(total_gazettes) / 10)

        for page in range(1, total_pages + 1):
            yield Request(
                url=f"http://www.sobral.ce.gov.br/diario/pesquisa/index/pg:{page}",
                callback=self.parse_gazettes,
            )

    def parse_gazettes(self, response):
        gazette_results = response.xpath("//ul[@class = 'resultado-busca']//article")
        for gazette in gazette_results:
            link = response.urljoin(
                gazette.xpath("./a[contains(@href, '.pdf')]/@href").get()
            )
            title = gazette.xpath("./a/h5/text()").get()
            edition_number = re.search(r"Diário Oficial Nº (\d+)", title).group(1)
            extra_edition = "Suplementar" in title
            gazette_extract = gazette.xpath(".//p/text()").get()
            date = dateparser.parse(
                re.search(r"(\d{2}/\d{2}/\d{4})", gazette_extract).group(1),
                date_formats=["%d%m%Y"],
            ).date()
            yield Gazette(
                date=date,
                file_urls=[link],
                edition_number=edition_number,
                is_extra_edition=extra_edition,
                power="executive_legislative",
            )
