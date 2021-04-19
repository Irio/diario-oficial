from urllib.parse import urljoin

import dateparser
import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider

START_URL = "http://www.paulinia.sp.gov.br/semanarios"


class SpPauliniaSpider(BaseGazetteSpider):
    name = "sp_paulinia"
    TERRITORY_ID = "3536505"

    start_urls = [START_URL]

    def parse(self, response):
        for year_href in response.css('a[id^="corpo_lnkItem"]::attr(href)').extract():
            year_value = year_href.split("'")[1]
            yield scrapy.FormRequest.from_response(
                response,
                formdata={"__EVENTTARGET": year_value},
                callback=self.parse_gazettes,
            )

    def parse_gazettes(self, response):
        for link in response.css('a[href^="AbreSemanario"]'):
            datestamp, edition, edition_type = (
                link.css("::text").get().strip().split(" - ")
            )
            date = dateparser.parse(datestamp, languages=["pt"]).date()
            href = link.css("::attr(href)").get()
            yield Gazette(
                date=date,
                is_extra_edition=("Extra" in edition_type),
                power="executive_legislative",
                file_urls=[urljoin(START_URL, href)],
            )
