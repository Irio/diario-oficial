from datetime import date, datetime
import re

import dateparser
from scrapy import Request
from scrapy.exceptions import CloseSpider

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class RjBelfordRoxoSpider(BaseGazetteSpider):
    TERRITORY_ID = "3300456"

    allowed_domains = ["prefeituradebelfordroxo.rj.gov.br"]
    name = "rj_belford_roxo"
    start_urls = ["https://prefeituradebelfordroxo.rj.gov.br/atos-oficiais/"]
    start_date = date(2017, 1, 1)

    def parse(self, response):
        for link in response.css("article a"):
            if not self.is_valid_gazette(link):
                continue

            date = self.get_date(link)
            if not date or date < self.start_date:
                continue

            link_href = link.css("::attr(href)").get()

            power = self.get_power(link)
            if not power:
                continue

            yield Gazette(
                date=date,
                file_urls=[link_href],
                is_extra_edition=False,
                territory_id=self.TERRITORY_ID,
                power=power,
                scraped_at=datetime.utcnow(),
            )

    def is_valid_gazette(self, link):
        link_text = link.css("::text").get()

        return link_text is not None and (
            self.is_executive(link) or self.is_legislative(link)
        )

    def get_power(self, link):
        if self.is_executive(link):
            return "executive"

        if self.is_legislative(link):
            return "legislative"

        return None

    def get_date(self, link):
        if self.is_executive_edge_case(link):
            return self.extract_date_from_edge_case(link)

        return self.extract_date_from_str(link)

    def is_executive(self, link):
        link_text = link.css("::text").get()
        return self.is_executive_edge_case(link) or link_text.lower().startswith(
            "atos oficiais"
        )

    # Segundo|Terceiro caderno cases
    def is_executive_edge_case(self, link):
        link_text = link.css("::text").get()
        return "caderno" in link_text.lower()

    def is_legislative(self, link):
        link_text = link.css("::text").get()
        return link_text.lower().startswith("boe")

    def extract_date_from_str(self, link):
        link_text = link.css("::text").get()

        date_re = re.search(r"\d{2}\/\d{2}\/\d{2,4}", link_text)  # DD/MM/YYYY
        if not date_re:
            return None

        date_str = date_re.group(0)

        parsed_date = dateparser.parse(date_str, languages=["pt"])
        # There is a case of a gazette in a day that doesn't exists (31/04)
        # which can make this parse fail. Hence, this validation
        if not parsed_date:
            return None

        return parsed_date.date()

    # Segundo|Terceiro caderno case
    def extract_date_from_edge_case(self, link):
        link_text = link.css("::text").get()

        date_re = re.search(r"\d{2}\/\d{2}", link_text)  # DD/MM
        if not date_re:
            return None

        partial_date_str = date_re.group(0)

        preceding_sibling = link.xpath("preceding-sibling::a")
        preceding_sibling_date = self.extract_date_from_str(preceding_sibling)
        if not preceding_sibling_date:
            return None

        date_str = f"{partial_date_str}/{preceding_sibling_date.year}"
        return dateparser.parse(date_str, languages=["pt"]).date()
