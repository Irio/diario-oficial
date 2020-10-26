# -*- coding: utf-8 -*-
from dateparser import parse

import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class SpJundiaiSpider(BaseGazetteSpider):
    TERRITORY_ID = "3525904"
    name = "sp_jundiai"
    allowed_domains = ["jundiai.sp.gov.br"]
    start_urls = ["https://imprensaoficial.jundiai.sp.gov.br/"]

    def parse(self, response):
        gazettes = response.css("#lista-edicoes li.edicao-atual")
        for gazette in gazettes:
            gazette_url = gazette.css("a::attr(href)").extract_first()
            if gazette_url:
                yield scrapy.Request(gazette_url, callback=self.parse_gazette)

        for next_page_url in response.css("div.paginacao a::attr(href)"):
            yield response.follow(next_page_url, callback=self.parse)

    def parse_gazette(self, response):
        gazette_date = parse(
            response.css(".edicao-data::text").extract_first(""), languages=["pt"]
        ).date()
        file_urls = response.css("div.edicao-download a::attr(href)").extract()
        is_extra_edition = (
            "extra" in response.css("div.edicao-titulo::text").extract_first("").lower()
        )
        power = "executive"

        yield Gazette(
            date=gazette_date,
            file_urls=file_urls,
            is_extra_edition=is_extra_edition,
            power=power,
        )
