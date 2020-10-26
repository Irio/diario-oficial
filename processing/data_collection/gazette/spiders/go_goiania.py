from dateparser import parse
import datetime as dt

import re
import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class GoGoianiaSpider(BaseGazetteSpider):
    TERRITORY_ID = "5208707"
    name = "go_goiania"
    allowed_domains = ["goiania.go.gov.br"]
    start_urls = ["http://www4.goiania.go.gov.br/portal/site.asp?s=775&m=2075"]
    gazettes_list_url = (
        "http://www.goiania.go.gov.br/shtml//portal/casacivil/lista_diarios.asp?ano={}"
    )

    def parse(self, response):
        current_year = dt.date.today().year
        for year in range(current_year, 2014, -1):
            url = self.gazettes_list_url.format(year)
            yield scrapy.Request(url, self.parse_year)

    def parse_year(self, response):
        # The page with the list of gazettes is simply a table with links
        links = response.css("a")
        items = []
        for link in links:
            url = link.css("::attr(href)").extract_first()
            if url[-4:] != ".pdf":
                continue

            url = response.urljoin(url)
            # Apparently, Goiânia doesn't have a separate gazette for executive and legislative
            power = "executive_legislature"
            link_text = link.css("::text").extract_first()
            if link_text is None:
                continue

            date = re.match(".*(\d{2} .* de \d{4})", link_text)[1]
            # Extra editions are marked either with 'suplemento' or 'comunicado'
            is_extra_edition = (
                "suplemento" in link_text.lower() or "comunicado" in link_text.lower()
            )
            date = parse(date.split("-")[0], languages=["pt"]).date()
            items.append(
                Gazette(
                    date=date,
                    file_urls=[url],
                    is_extra_edition=is_extra_edition,
                    power=power,
                )
            )
        return items
