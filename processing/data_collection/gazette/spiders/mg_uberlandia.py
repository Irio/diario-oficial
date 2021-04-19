# -*- coding: utf-8 -*-
import scrapy
import datetime as dt
import re
from gazette.items import Gazette


class MgUberlandiaSpider(scrapy.Spider):
    MUNICIPALITY_ID = 3170206
    name = "mg_uberlandia"
    allowed_domains = ["uberlandia.mg.gov.br"]
    start_urls = ["http://www.uberlandia.mg.gov.br/?pagina=Conteudo&id=39"]

    def parse(self, response):
        urls = response.css(
            "#home table[align*=right] td[style*=vertical-align] a::attr(href)"
        ).extract()
        urls = self.last_four_years(urls)
        for url in urls:
            yield scrapy.Request(url, self.parse_year)

    def parse_year(self, response):
        url_months = self.links_months(response)
        for url in url_months:
            yield scrapy.Request(url, self.parse_month)

    def parse_month(self, response):
        url_issues = response.xpath(
            '//a[contains(@href,"http://www.uberlandia.mg.gov.br/uploads")]'
        )
        dates = self.list_dates(response)
        items = []

        for i, url in enumerate(url_issues):
            url_issue = url.xpath("@href").extract_first()
            power = "executive_legislature"
            try:
                date = dt.datetime.strptime(dates[i], "%d/%m/%Y")
            except:
                date = None
            items.append(
                Gazette(
                    date=date,
                    file_urls=[url_issue],
                    is_extra_edition=False,
                    municipality_id=self.MUNICIPALITY_ID,
                    power=power,
                    scraped_at=dt.datetime.utcnow(),
                )
            )
        return items

    def links_months(self, response):
        variants = [
            '//div[contains(@class,"colunaConteudo")]/p/strong/span/span/a/@href',
            '//div[contains(@class,"colunaConteudo")]/p/strong/span/span/span/a/@href',
            '//div[contains(@class,"colunaConteudo")]/p/strong/a/@href',
            '//div[contains(@class,"colunaConteudo")]/p/a/@href',
            '//div[contains(@class,"colunaConteudo")]/p/span/span/strong/a/@href',
            '//div[contains(@class,"colunaConteudo")]/p/span/span/span/a/@href',
        ]
        urls_return = []
        for variant in variants:
            urls = response.xpath(variant).extract()
            for url in urls:
                urls_return.append(url)
        return urls_return

    def list_dates(self, response):
        variants = ["//p/span/text()", "//p/span/span/text()", "//p/text()"]
        dates = []
        for variant in variants:
            results = response.xpath(variant).extract()
            for result in results:
                d = re.findall("\d{2}/\d{2}/\d{4}", result)
                if len(d) == 1:
                    dates.append(d[0])
        return sorted(dates, reverse=True)

    def last_four_years(self, urls):
        """ proposed in https://github.com/okfn-brasil/diario-oficial/issues/23 """
        if len(urls) < 4:
            return urls
        urls_return = []
        for url in urls:
            urls_return.append(url)
            if len(urls_return) == 4:
                return urls_return
