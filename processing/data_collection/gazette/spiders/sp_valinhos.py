# -*- coding: utf-8 -*-
import datetime
import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class SpValinhosSpider(BaseGazetteSpider):
    TERRITORY_ID = "3556206"
    name = "sp_valinhos"
    allowed_domains = ["valinhos.sp.gov.br"]
    base_urls = ["http://www.valinhos.sp.gov.br"]
    selector_url = "http://www.valinhos.sp.gov.br/boletins?title=&field_boletim_publicacao_value%5Bvalue%5D%5Bmonth%5D={}&field_boletim_publicacao_value%5Bvalue%5D%5Byear%5D={}"

    def parse(self, response):
        today = datetime.date.today()
        next_year = today.year + 1
        for year in range(2015, next_year):
            for month in range(1, 13):
                if year == today.year and month > today.month:
                    return

                url = self.selector_url.format(month, year)
                yield scrapy.Request(url, self.parse_month_page)

    def parse_month_page(self, response):
        items = []
        blocks = response.xpath('//*[@id="block-system-main"]/div/div[2]/div/ul/li')
        for edition in blocks:
            span = edition.xpath("//div/span/div/div[2]/a")
            url = span.css("::attr(href)").extract_first().replace("../", "")

            spanDate = edition.xpath("//div/span/div/div[2]/span")
            date = spanDate.css("::attr(content)").extract_first()

            items.append(
                Gazette(
                    date=date,
                    file_urls=[url],
                    territory_id=self.TERRITORY_ID,
                    scraped_at=datetime.datetime.utcnow(),
                )
            )
        return items
