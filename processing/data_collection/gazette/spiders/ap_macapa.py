from urllib.parse import urlencode
import datetime as dt

from dateparser import parse
import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class ApMacapaSpider(BaseGazetteSpider):
    TERRITORY_ID = "1600303"
    name = "ap_macapa"
    allowed_domains = ["macapa.ap.gov.br"]
    start_urls = ["https://macapa.ap.gov.br/diarios-oficiais/"]

    def start_requests(self):
        today = dt.date.today()

        base_url = "https://macapa.ap.gov.br/"
        params = {
            "s": "",
            "post_type": "official_diaries",
            "official_diary_initial_date": "01/01/2020",
            "official_diary_final_date": today.strftime("%d/%m/%Y"),
        }
        encoded_params = urlencode(params)
        initial_url = f"{base_url}?{encoded_params}"

        yield scrapy.Request(initial_url)

    def parse(self, response):
        gazettes = response.css(".panel")
        for gazette in gazettes:
            gazette_raw_date = gazette.css("a h4").re_first(
                r"[Dd][Ee] (\d{2} [Dd][Ee] [\w]+ [Dd][Ee] \d{4})"
            )
            if gazette_raw_date:
                gazette_date = parse(gazette_raw_date, languages=["pt"]).date()
                yield Gazette(
                    date=gazette_date,
                    file_urls=gazette.css("a::attr(href)").getall(),
                    is_extra_edition=False,
                    territory_id=self.TERRITORY_ID,
                    power="executive",
                    scraped_at=dt.datetime.utcnow(),
                )

        next_pages_urls = response.css("a.page-numbers::attr(href)").getall()
        for next_page_url in next_pages_urls:
            yield scrapy.Request(next_page_url)
