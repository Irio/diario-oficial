# -*- coding: utf-8 -*-
from scrapy import Request
from gazette.spiders.base import BaseGazetteSpider
from gazette.items import Gazette
import dateparser


class SpBauruSpider(BaseGazetteSpider):
    custom_settings = {"MEDIA_ALLOW_REDIRECTS": True}

    TERRITORY_ID = "3506003"
    BASE_XPATH = "//div[@class='col-md-12']"
    name = "sp_bauru"
    allowed_domains = ["bauru.sp.gov.br"]
    start_urls = ["https://www2.bauru.sp.gov.br/juridico/diariooficial.aspx"]

    def parse(self, response):
        avaliable_years = response.xpath(
            f"{self.BASE_XPATH}" "/ul/li/a/text()"
        ).extract()

        for year in avaliable_years:
            yield Request(url=f"{response.url}?a={year}", callback=self.parse_year)

    def parse_year(self, response):

        months_links = response.xpath(
            f"{self.BASE_XPATH}" "/ul/li/ul/li/a/@href"
        ).extract()

        for month_link in months_links:
            yield Request(
                url=f"https://www2.bauru.sp.gov.br/juridico/{month_link}",
                callback=self.parse_month,
            )

    def parse_month(self, response):
        gazettes_seletor = response.xpath(f"{self.BASE_XPATH}" "/ul/li/ul/li/ul/li/a")

        for gazette_seletor in gazettes_seletor:
            date = dateparser.parse(
                gazette_seletor.xpath("//b/text()").get().split(":")[0].strip(),
                date_formats=["%d/%m/%Y"],
            ).date()
            url = response.urljoin(gazette_seletor.xpath("@href").get())

            yield Gazette(
                date=date,
                file_urls=[url],
                is_extra_edition="especial" in url.lower(),
                power="executive",
            )
