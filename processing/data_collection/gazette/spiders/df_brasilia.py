from datetime import datetime
import re

import dateparser
from scrapy import Request

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class DfBrasiliaSpider(BaseGazetteSpider):
    TERRITORY_ID = "5300108"
    name = "df_brasilia"

    GAZETTE_URL = "http://dodf.df.gov.br/listar"
    DATE_REGEX = r"[0-9]{2}-[0-9]{2}[ -][0-9]{2,4}"
    EXTRA_EDITION_TEXT = "EDICAO EXTR"
    PDF_URL = "http://dodf.df.gov.br/index/visualizar-arquivo/?pasta={}&arquivo={}"

    def start_requests(self):
        """Requests page that has a list of all available years."""
        yield Request(self.GAZETTE_URL, callback=self.parse_year_list)

    def parse_year_list(self, response):
        """Parses available years to request list of available months for each year."""
        years_available = response.css(
            "#local-arquivos .arquivo::attr(data-file)"
        ).getall()

        for year in years_available:
            yield Request(
                f"{self.GAZETTE_URL}?dir={year}",
                meta={"year": year},
                callback=self.parse_year,
            )

    def parse_year(self, response):
        """Parses available months to request list of available dates for each month.
        """
        months_available = response.json().get("data", [])
        year = response.meta["year"]

        for month in months_available:
            yield Request(
                f"{self.GAZETTE_URL}?dir={year}/{month}",
                meta={"month": month, "year": year},
                callback=self.parse_month,
            )

    def parse_month(self, response):
        """Parses available dates to request a list of documents for each date."""
        month, year = response.meta["month"], response.meta["year"]
        dates = response.json().get("data", [])

        for gazette_name in dates.values():
            url = f"{self.GAZETTE_URL}?dir={year}/{month}/{gazette_name}"
            yield Request(url, callback=self.parse_gazette)

    def parse_gazette(self, response):
        """Parses list of documents to request each one for the date."""
        json_response = response.json()

        if not json_response:
            self.logger.warning(f"Document not found in {response.url}")
            return

        json_dir = json_response["dir"]

        date = re.search(self.DATE_REGEX, json_dir).group()
        date = dateparser.parse(date, settings={"DATE_ORDER": "DMY"})
        is_extra_edition = self.EXTRA_EDITION_TEXT in json_dir
        path = json_dir.replace("/", "|")

        json_data = json_response["data"]
        file_urls = [self.PDF_URL.format(path, url.split("/")[-1]) for url in json_data]

        yield Gazette(
            date=date,
            file_urls=file_urls,
            is_extra_edition=is_extra_edition,
            territory_id=self.TERRITORY_ID,
            scraped_at=datetime.utcnow(),
            power="executive_legislative",
        )
