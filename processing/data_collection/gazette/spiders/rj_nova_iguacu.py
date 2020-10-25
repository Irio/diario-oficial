import datetime as dt

import scrapy
from dateparser import parse
from dateutil.rrule import rrule, DAILY

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class RjNovaIguacu(BaseGazetteSpider):
    TERRITORY_ID = "3303500"
    name = "rj_nova_iguacu"
    allowed_domains = ["novaiguacu.rj.gov.br"]

    def start_requests(self):
        starting_date = dt.date(2015, 1, 1)
        ending_date = dt.date.today()
        base_url = "http://www.novaiguacu.rj.gov.br/diario-oficial/?data="
        for date in rrule(DAILY, dtstart=starting_date, until=ending_date):
            yield scrapy.Request(f"{base_url}{date.isoformat()}")

    def parse(self, response):
        """
        @url http://www.novaiguacu.rj.gov.br/diario-oficial/?data=2018-05-16
        @returns items 1 1
        @scrapes date file_urls is_extra_edition territory_id power scraped_at
        """
        link = response.css("div.caption h4 a")
        if not link:
            return
        url = link.css("::attr(href)").extract_first()
        date = link.re_first(r"\d{1,2}/\d{1,2}/\d{2}(?:\d{2})?")
        date = parse(date, languages=["pt"]).date()
        yield Gazette(
            date=date,
            file_urls=[url],
            is_extra_edition=False,
            territory_id=self.TERRITORY_ID,
            power="executive",
            scraped_at=dt.datetime.utcnow(),
        )
