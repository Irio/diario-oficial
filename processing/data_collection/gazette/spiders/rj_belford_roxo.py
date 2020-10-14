from datetime import datetime
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

    def parse(self, response):
        for link in response.xpath(
            '//article[contains(@class, "post-listing")]//div[@class="entry"]/p/a'
        ):
            date = self.get_date(link)
            if not date:
                continue

            path_to_gazette = link.css("::attr(href)").extract_first()
            if not path_to_gazette:
                continue

            # executive only, apparently
            is_extra_edition = False

            yield Gazette(
                date=date,
                file_urls=[path_to_gazette],
                is_extra_edition=is_extra_edition,
                territory_id=self.TERRITORY_ID,
                power="executive",
                scraped_at=datetime.utcnow(),
            )

    @staticmethod
    def get_date(link):
        link_text = link.css("::text").extract()

        date_re = re.search(r"\d{2}\/\d{2}\/\d{2,4}", link_text)
        if not date_re:
            return None

        date_str = date_re.group(0)
        return dateparser.parse(date_str, languages=["pt"]).date()
