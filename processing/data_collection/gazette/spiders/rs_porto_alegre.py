from dateparser import parse
import datetime as dt

import scrapy

from gazette.items import Gazette


class RsPortoAlegreSpider(scrapy.Spider):
    MUNICIPALITY_ID = '4314902'
    name = 'rs_porto_alegre'
    allowed_domains = ['portoalegre.rs.gov.br']
    start_urls = ['http://www2.portoalegre.rs.gov.br/dopa/']

    def parse(self, response):
        """
        @url http://www2.portoalegre.rs.gov.br/dopa/
        @returns requests 48
        """
        selector = (
            '//ul[contains(@id, "menucss")]'
            '/descendant::*[contains(text(), "Diário Oficial {}")]'
            '/parent::*/descendant::li/a'
        )
        current_year = dt.date.today().year
        for year in range(current_year, 2014, -1):
            urls = response.xpath(selector.format(year) + '/attribute::href').extract()
            urls = [response.urljoin(url) for url in urls]
            for url in urls:
                yield scrapy.Request(url, self.parse_month_page)

    def parse_month_page(self, response):
        """
        @url http://www2.portoalegre.rs.gov.br/dopa/default.php?p_secao=1431
        @returns items 58 58
        @scrapes date file_urls is_extra_edition municipality_id power scraped_at
        """
        links = response.css('#conteudo a')
        items = []
        for link in links:
            url = link.css('::attr(href)').extract_first()
            if url[-4:] != '.pdf':
                continue

            url = response.urljoin(url)
            power = 'executive' if 'executivo' in url.lower() else 'legislature'
            date = link.css('::text').extract_first()
            is_extra_edition = 'extra' in date.lower()
            date = parse(date.split('-')[0], languages=['pt']).date()
            items.append(
                Gazette(
                    date=date,
                    file_urls=[url],
                    is_extra_edition=is_extra_edition,
                    municipality_id=self.MUNICIPALITY_ID,
                    power=power,
                    scraped_at=dt.datetime.utcnow(),
                )
            )
        return items
