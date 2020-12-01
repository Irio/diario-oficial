from datetime import date, datetime

import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class ImprensaOficialSpider(BaseGazetteSpider):
    @staticmethod
    def _get_next_month(current_date):
        month = (current_date.month % 12) + 1
        year = current_date.year + (current_date.month + 1 > 12)
        return date(year, month, 1)

    def start_requests(self):
        current_date = self.start_date
        end_date = date.today()
        while current_date <= end_date:
            year_month = current_date.strftime("%Y/%m")  # like 2015/01
            current_date = self._get_next_month(current_date)
            yield scrapy.Request(
                self.url_base.format(year_month), callback=self.extract_gazette_links
            )

    def extract_gazette_links(self, response):
        for a in response.css("h2 a"):
            yield scrapy.Request(a.attrib["href"], dont_filter=True)

        # pagination exists when the button "Publicações mais antigas" is in the page
        another_page = response.xpath(
            ".//a[contains(text(), 'Publicações mais antigas')]/@href"
        ).get()
        if another_page:
            yield scrapy.Request(another_page, callback=self.extract_gazette_links)

    def parse(self, response):
        file_url = self.url_base.format(
            response.css("div.entry-content a::attr(href)").re_first(
                r"arquivo=\.\.\/(.*)"
            )
        )
        gazette_date = response.css("span.posted-on a time::attr(datetime)").get()
        gazette_date = datetime.strptime(gazette_date, "%Y-%m-%dT%H:%M:%S%z").date()

        yield Gazette(
            date=gazette_date,
            file_urls=[file_url],
            is_extra_edition=False,
            power="executive",
        )
