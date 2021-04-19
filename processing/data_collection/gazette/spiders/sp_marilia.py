# -*- coding: utf-8 -*-
from dateparser import parse
import datetime as dt

import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class SpMariliaSpider(BaseGazetteSpider):
    TERRITORY_ID = "3529005"
    name = "sp_marilia"
    allowed_domains = ["marilia.sp.gov.br"]
    start_urls = ["https://www.marilia.sp.gov.br/portal/diario-oficial"]

    def parse(self, response):
        gazettes = response.css(".d_e_modelo_diario")
        for gazette in gazettes:
            gazette_url = gazette.css("a::attr(href)").getall()[1]
            is_extra_edition = gazette.css(".d_e_btextra::text")[1:]
            if gazette_url:
                gazette_date = parse(
                    gazette.css(".d_e_cont_bt span::text").get()[1:11], languages=["pt"]
                ).date()
                file_urls = response.urljoin(gazette.css("a::attr(href)").getall()[1])
                power = "executive"

                yield Gazette(
                    date=gazette_date,
                    file_urls=[file_urls],
                    is_extra_edition=is_extra_edition,
                    territory_id=self.TERRITORY_ID,
                    power=power,
                    scraped_at=dt.datetime.utcnow(),
                )

        for next_page_url in response.css("div .d_e_cont_pag a::attr(href)").getall():

            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)
