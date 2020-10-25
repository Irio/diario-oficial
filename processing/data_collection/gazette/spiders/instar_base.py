import datetime as dt

from dateparser import parse
from scrapy import Request

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class BaseInstarSpider(BaseGazetteSpider):
    def parse(self, response):
        page_url = response.urljoin("{page}/0/0/0/0/")
        last_page = int(
            response.xpath("//select[@id='select']/option[last()]/text()").get()
        )
        if last_page is not None:
            for page in range(2, 1 + last_page):
                yield Request(
                    page_url.format(page=page), callback=self.parse_editions_page
                )
        yield from self.parse_editions_page(response)

    def parse_editions_page(self, response):
        diarios = response.css(".d_e_modelo_diario")
        for diario in diarios:
            href = diario.xpath('.//a[contains(@href, "downloads")]/@href').get()
            date = diario.xpath("div/span/text()").re_first("\d{2}/\d{2}/\d{4}")
            is_extra_edition = (
                diario.xpath(".//span[contains(./text(), 'Extra')]").get() is not None
            )
            yield Gazette(
                date=parse(date, languages=["pt"]).date(),
                file_urls=[response.urljoin(href)],
                is_extra_edition=is_extra_edition,
                territory_id=self.TERRITORY_ID,
                power="executive_legislature",
                scraped_at=dt.datetime.utcnow(),
            )
