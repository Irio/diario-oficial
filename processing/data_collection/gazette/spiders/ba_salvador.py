# -*- coding: utf-8 -*-
import datetime
import re
import urllib.parse

import dateparser
import scrapy

from gazette.items import Gazette
from gazette.settings import ITEM_PIPELINES
from gazette.spiders.base import BaseGazetteSpider


class BaSalvadorSpider(BaseGazetteSpider):
    TERRITORY_ID = "2927408"
    name = "ba_salvador"
    allowed_domains = ["salvador.ba.gov.br"]
    power = "executive"

    @classmethod
    def update_settings(cls, settings):
        pipelines = settings["ITEM_PIPELINES"]
        pipelines[
            "gazette.spiders.ba_salvador.BaSalvadorExtraEditionItemPipeline"
        ] = 1000
        super().update_settings(settings)

    def start_requests(self):
        # According to their website, they have gazettes available from 2001-01-01
        initial_search_parameters = {
            "filterDateFrom": "2001-01-01",
            "filterDateTo": datetime.date.today().strftime("%Y-%m-%d"),
            "option": "com_dmarticlesfilter",
            "view": "articles",
            "Itemid": "3",
            "userSearch": "1",
            "limstart": "0",
            "limitstart": "10",
        }
        encoded_params = urllib.parse.urlencode(initial_search_parameters)
        base_url = "http://www.dom.salvador.ba.gov.br/index.php"
        first_page_url = f"{base_url}?{encoded_params}"
        yield scrapy.Request(first_page_url)

    def parse(self, response):
        for gazette in response.css(".dmarticlesfilter_results_title"):
            gazette_date = gazette.css(
                "#dmarticlesfilter_results_date::text"
            ).extract_first("")
            gazette_url = gazette.css("a::attr(href)").extract_first()

            yield scrapy.Request(
                response.urljoin(gazette_url),
                meta={"gazette_date": gazette_date},
                callback=self.parse_gazette,
            )

        for href in response.css(".paginacao a::attr(href)"):
            yield response.follow(href, callback=self.parse)

    def parse_gazette(self, response):
        parsed_date = dateparser.parse(
            response.meta.get("gazette_date"), settings={"DATE_ORDER": "YMD"}
        )
        pdf_url = response.css("#PDFId embed::attr(src)").extract_first()

        yield Gazette(
            date=parsed_date.date(),
            file_urls=[pdf_url],
            territory_id=self.TERRITORY_ID,
            power=self.power,
            scraped_at=datetime.datetime.utcnow(),
        )


class BaSalvadorExtraEditionItemPipeline:
    def process_item(self, item, spider):
        item["is_extra_edition"] = False

        # The only indication if the gazette is an extra edition is a
        # red strip over the first page of the PDF with the text 'EDIÇÃO EXTRA'
        # Unfortunately pdftotext is unable to get the whole word and after some
        # tests comparing some gazettes, this regex seems to be enough to identify an
        # extra edition. But I can't guarantee this is 100% accurate. Maybe older
        # editions has a different pattern.
        if re.findall("T[\s]+RA", item.get("source_text", "")):
            item["is_extra_edition"] = True

        return item
