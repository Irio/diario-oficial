import json
import re
from datetime import date, datetime

import dateparser
from dateutil.rrule import DAILY, rrule
from fake_useragent import UserAgent
import scrapy
from gazette.items import Gazette
from scrapy.exceptions import NotConfigured


class BaseGazetteSpider(scrapy.Spider):
    def __init__(self, start_date=None, *args, **kwargs):
        super(BaseGazetteSpider, self).__init__(*args, **kwargs)

        if not hasattr(self, "TERRITORY_ID"):
            raise NotConfigured("Please set a value for `TERRITORY_ID`")

        if start_date is not None:
            try:
                self.start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
                self.logger.info(f"Collecting gazettes after {self.start_date}")
            except ValueError:
                self.logger.exception(
                    f"Unable to parse {start_date}. Use %Y-%m-d date format."
                )
                raise
        else:
            self.logger.info("Collecting all gazettes available")


class SigpubGazetteSpider(BaseGazetteSpider):
    """www.diariomunicipal.com.br (Sigpub) base spider

    Documents obtained by this kind of spider are text-PDFs with many cities in it.
    That's because the websites are usually made for associations of cities.
    
    TODO:
        - All variations have a "possible" start date of 01/01/2009, but that may cause
        many unnecessary requests to be made if they actually start making available
        documents later. Some investigation for the start date of each website needs to
        be made in this case.

    Observations:
        - These websites have an "Advanced Search", but they are protected by ReCaptcha.
    """

    custom_settings = {"USER_AGENT": UserAgent().random}
    start_date = date(2009, 1, 1)

    def start_requests(self):
        """Requests start page where the calendar widget is available."""
        yield scrapy.Request(self.CALENDAR_URL, callback=self.parse_calendar)

    def parse_calendar(self, response):
        """Makes requests for each date to see if a document is available."""
        default_form_fields = {
            "calendar[_token]": response.xpath(
                "//input[@id='calendar__token']/@value"
            ).get()
        }
        for date, date_form_fields in self.available_dates_form_fields():
            formdata = {**default_form_fields, **date_form_fields}

            yield scrapy.FormRequest(
                url=response.urljoin("materia/calendario"),
                formdata=formdata,
                meta={"date": date, "edition_type": "regular"},
                callback=self.parse_gazette_info,
            )
            yield scrapy.FormRequest(
                url=response.urljoin("materia/calendario/extra"),
                formdata=formdata,
                meta={"date": date, "edition_type": "extra"},
                callback=self.parse_gazette_info,
            )

    def parse_gazette_info(self, response):
        """Parses document availability endpoint and gets document URL if available."""
        body = json.loads(response.text)
        meta = response.meta

        if "error" in body:
            self.logger.debug(
                f"{meta['edition_type'].capitalize()} Gazette not available for {meta['date'].date()}"
            )
            return

        for edition in body["edicao"]:
            url = f"{body['url_arquivos']}{edition['link_diario']}.pdf"
            yield Gazette(
                date=meta["date"].date(),
                file_urls=[url],
                territory_id=self.TERRITORY_ID,
                power="executive_legislative",
                is_extra_edition=(meta["edition_type"] == "extra"),
                scraped_at=datetime.utcnow(),
                edition_number=edition.get("numero_edicao", ""),
            )

    def available_dates_form_fields(self):
        """Generates dates and corresponding form fields for availability endpoint."""
        available_dates = rrule(freq=DAILY, dtstart=self.start_date, until=date.today())
        for query_date in available_dates:
            form_fields = {
                "calendar[day]": str(query_date.day),
                "calendar[month]": str(query_date.month),
                "calendar[year]": str(query_date.year),
            }
            yield query_date, form_fields


class FecamGazetteSpider(BaseGazetteSpider):

    URL = "https://www.diariomunicipal.sc.gov.br/site/"
    total_pages = None

    def start_requests(self):
        yield scrapy.Request(
            f"{self.URL}?q={self.FECAM_QUERY}", callback=self.parse_pagination
        )

    def parse_pagination(self, response):
        """
        This parse function is used to get all the pages available and
        return request object for each one
        """
        return [
            scrapy.Request(
                f"{self.URL}?q={self.FECAM_QUERY}&Search_page={i}", callback=self.parse
            )
            for i in range(1, self.get_last_page(response) + 1)
        ]

    def parse(self, response):
        """
        Parse each page from the gazette page.
        """
        # Get gazzete info
        documents = self.get_documents_links_date(response)
        for d in documents:
            yield self.get_gazette(d)

    def get_documents_links_date(self, response):
        """
        Method to get all the relevant documents list and their dates from the page
        """
        documents = []
        titles = response.css("div.row.no-print h4")
        for title in titles:
            title_sibling_link = title.xpath("following-sibling::a[2]")
            if "[Abrir/Salvar Original]" in title_sibling_link.xpath("./text()").get():
                link = title_sibling_link.xpath("./@href").get().strip()
            else:
                link = title.xpath("./a/@href").get().strip()
            date = (
                title.xpath("following-sibling::span[1]")
                .re_first("\d{2}/\d{2}/\d{4}")
                .strip()
            )
            documents.append((link, date))
        return documents

    @staticmethod
    def get_last_page(response):
        """
        Get the last page number available in the pages navigation menu
        """
        href = response.xpath(
            "/html/body/div[1]/div[4]/div[4]/div/div/ul/li[14]/a/@href"
        ).get()
        result = re.search("Search_page=(\d+)", href)
        if result is not None:
            return int(result.groups()[0])

    def get_gazette(self, document):
        """
        Transform the tuple returned by get_documents_links_date and returns a
        Gazette item
        """
        if document[1] is None or len(document[1]) == 0:
            raise "Missing document date"
        if document[0] is None or len(document[0]) == 0:
            raise "Missing document URL"

        return Gazette(
            date=dateparser.parse(document[1], languages=("pt",)).date(),
            file_urls=(document[0],),
            territory_id=self.TERRITORY_ID,
            scraped_at=datetime.utcnow(),
        )
