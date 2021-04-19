import datetime
import re

from dateparser import parse
from scrapy import Request

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class DfBrasiliaSpider(BaseGazetteSpider):
    TERRITORY_ID = "5300108"
    name = "df_brasilia"
    start_date = datetime.date(1967, 12, 25)

    GAZETTE_URL = "http://dodf.df.gov.br/listar"
    DATE_REGEX = r"[0-9]{2}-[0-9]{2}[ -][0-9]{2,4}"
    EXTRA_EDITION_TEXT = "EDICAO EXTR"
    PDF_URL = "https://dodf.df.gov.br/index/visualizar-arquivo/?pasta={}&arquivo={}"

    def start_requests(self):
        """Requests page that has a list of all available years."""
        initial_year = self.start_date.year
        end_year = datetime.date.today().year
        for year in range(initial_year, end_year + 1):
            yield Request(
                f"{self.GAZETTE_URL}?dir={year}",
                meta={"year": year},
                callback=self.parse_year,
            )

    def parse_year(self, response):
        """Parses available months to request list of available dates for each month."""
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
            date = re.search(self.DATE_REGEX, gazette_name).group()
            date = parse(date, settings={"DATE_ORDER": "DMY"}).date()

            if date < self.start_date:
                continue

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
        date = parse(date, settings={"DATE_ORDER": "DMY"}).date()
        is_extra_edition = self.EXTRA_EDITION_TEXT in json_dir
        path = json_dir.replace("/", "|")

        json_data = json_response["data"]
        file_urls = [self.PDF_URL.format(path, url.split("/")[-1]) for url in json_data]

        yield Gazette(
            date=date,
            file_urls=file_urls,
            is_extra_edition=is_extra_edition,
            power="executive_legislative",
        )
