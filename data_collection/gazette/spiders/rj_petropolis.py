import datetime
import re
from urllib.parse import urljoin

import dateparser
import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class RjPetropolis(BaseGazetteSpider):
    """
    The petropolis city gazettes are organized on the site in a directory-based structure (year/month/items)

    The gazettes website has many cases that are outside the standard
    Some examples are:
        - edition 4406 of 2014-02-11 (recovered by the spider)
        - edition 4526 of 2014-08-14 (recovered)
        - month page of 2006-12 (recovered)
        - year page of 2002 (recovered)
        - edition 2377 of 2015-09 (not recovered, no date available)
        - edition 3392 of 2009-12-03 (not recovered, wrong writing)
    """

    TERRITORY_ID = "3303906"
    BASE_URL = "https://www.petropolis.rj.gov.br"

    name = "rj_petropolis"
    allowed_domains = ["petropolis.rj.gov.br"]
    start_urls = [
        f"{BASE_URL}/pmp/index.php/servicos-na-web/informacoes/diario-oficial/viewcategory/3-diario-oficial.html"
    ]
    start_date = datetime.date(2001, 10, 2)

    month_name_to_number = {
        "janeiro": 1,
        "fevereiro": 2,
        "marco": 3,
        "março": 3,
        "abril": 4,
        "maio": 5,
        "junho": 6,
        "julho": 7,
        "agosto": 8,
        "setembro": 9,
        "outubro": 10,
        "novembro": 11,
        "dezembro": 12,
    }

    def parse(self, response):
        for document in response.css("#col1 div table tr td b a"):
            year = int(document.css("::text").get())

            # yield a request only if the year is greater than the starting year
            if year >= self.start_date.year:
                year_url_sufix = document.css("::attr(href)").get()
                year_url = urljoin(self.BASE_URL, year_url_sufix)
                yield scrapy.Request(
                    url=year_url, callback=self.parse_month_page, meta={"year": year}
                )

    def parse_month_page(self, response):
        for document in response.css("#col1 div table tr td b a"):
            month_name = document.css("::text").get().lower()
            month = self.month_name_to_number.get(month_name)
            year = response.meta["year"]

            # yield a request only if the month and year are greater than the starting month and year
            if month and datetime.date(year, month, 1) >= datetime.date(
                self.start_date.year, self.start_date.month, 1
            ):
                month_url_sufix = document.css("::attr(href)").get()
                month_url = urljoin(self.BASE_URL, month_url_sufix)
                yield scrapy.Request(url=month_url, callback=self.parse_items_page)

    def parse_items_page(self, response):
        for document in response.css("#col1 div table"):
            if document.css(".jd_download_url"):
                document_url_sufix = document.css("a::attr(href)").get()
                document_url = urljoin(self.BASE_URL, document_url_sufix)
                file_url = document_url.replace(".html", ".pdf")

                text = " ".join(document.css("*::text").getall())
                text = re.sub(r"\s+", " ", text).strip()

                # being able to retrieve the date in both formats is important
                # because in some cases it is only available in one format
                date_match = re.search(
                    r"(\d{1,2}\/\d{1,2}\/\d{4})|(\d{1,2}.de.\w+.de.\d{4})",
                    text,
                    re.IGNORECASE,
                )

                is_extra_edition = bool(
                    re.search(r"suplemento|extra", text, re.IGNORECASE)
                )
                edition_number_match = re.search(r"^\d+", text)

                if date_match is not None and edition_number_match is not None:
                    edition_number = edition_number_match.group(0)
                    date = dateparser.parse(
                        date_match.group(0), languages=["pt"]
                    ).date()

                    yield Gazette(
                        date=date,
                        file_urls=[file_url],
                        is_extra_edition=is_extra_edition,
                        territory_id=self.TERRITORY_ID,
                        power="executive_legislative",
                        scraped_at=datetime.datetime.utcnow(),
                        edition_number=edition_number,
                    )
