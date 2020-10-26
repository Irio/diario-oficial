# coding=utf-8
import re
from datetime import datetime, date

import dateutil
import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class RnMossoroSpider(BaseGazetteSpider):

    name = "rn_mossoro"
    allowed_domains = ["jom.prefeiturademossoro.com.br"]

    TERRITORY_ID = "2408003"

    def __init__(self, start_date=None, end_date=None, *args, **kwargs):
        self.start_date = date(2008, 1, 1)
        self.end_date = date.today()

        super(RnMossoroSpider, self).__init__(start_date, end_date, *args, **kwargs)

        self.logger.debug(
            "Start date is {date}".format(date=self.start_date.isoformat())
        )
        self.logger.debug("End date is {date}".format(date=self.end_date.isoformat()))

    def start_requests(self):

        for year in range(self.start_date.year, self.end_date.year + 1):
            for month in range(self.start_date.month, self.end_date.month + 1):
                base_url = f"http://jom.prefeiturademossoro.com.br/{year}/{month}/"
                yield scrapy.Request(base_url)

    def parse(self, response):
        for entry in response.css("article.post.category-jom"):

            url = entry.css("a:first-of-type::attr(href)").get()
            datetime_meta = entry.css("time.published::attr(datetime)").get()
            entry_date = dateutil.parser.isoparse(datetime_meta).date()

            yield scrapy.Request(
                url, meta={"date": entry_date}, callback=self.parse_gazette
            )

        next_pages_links = response.css("a.page-numbers::attr(href)").getall()
        for link in next_pages_links:
            yield scrapy.Request(link)

    def parse_gazette(self, response):
        gazette_date = response.meta["date"]
        file_url = response.css(".wp-block-file__button::attr(href)").get()
        edition_regex = re.compile("JOM n\.º ([a-z0-9]+)$", re.IGNORECASE)
        edition = response.css("h1.entry-title::text").re_first(edition_regex)
        yield Gazette(
            date=gazette_date,
            edition_number=edition,
            file_urls=[file_url],
            is_extra_edition=False,
            territory_id=self.TERRITORY_ID,
            power="executive_legislative",
            scraped_at=datetime.utcnow(),
        )
