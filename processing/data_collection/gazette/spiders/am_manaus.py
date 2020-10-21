import dateparser

from scrapy import Request
from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class AmManausSpider(BaseGazetteSpider):
    TERRITORY_ID = "1302603"

    EXECUTIVE_URL = "http://dom.manaus.am.gov.br/diario-oficial-de-manaus"
    EXECUTIVE_NEXT_PAGE_URL = EXECUTIVE_URL + "/atct_topic_view?b_start:int={}&-C="
    LEGISLATIVE_URL = "http://www.cmm.am.gov.br/diario-oficial"

    EXECUTIVE_DATE_CSS = "td:first-child span::text"
    EXECUTIVE_GAZETTE_ROW_CSS = "table.listing tbody tr"
    EXECUTIVE_PDF_HREF_CSS = "td:nth-child(2) a::attr(href)"
    EXECUTIVE_PDF_TEXT_CSS = "td:nth-child(2) a:last-child::text"

    LEGISLATIVE_DATE_CSS = "td:first-child"
    LEGISLATIVE_GAZETTE_ROW_CSS = ".table-cmm tr"
    LEGISLATIVE_NEXT_PAGE_CSS = ".paging a.next::attr(href)"
    LEGISLATIVE_PDF_HREF_CSS = "td:last-child a::attr(href)"
    LEGISLATIVE_DATE_REGEX = r"[0-9]{2}/[0-9]{2}/[0-9]{4}"

    EXECUTIVE_LAST_PAGE = 1000
    EXECUTIVE_STEP = 20

    allowed_domains = ["manaus.am.gov.br", "cmm.am.gov.br"]
    name = "am_manaus"

    def start_requests(self):
        yield Request(self.EXECUTIVE_URL, self.parse_executive)
        yield Request(self.LEGISLATIVE_URL, self.parse_legislative)

    def parse_executive(self, response):
        for element in response.css(self.EXECUTIVE_GAZETTE_ROW_CSS):
            url = element.css(self.EXECUTIVE_PDF_HREF_CSS).extract_first()
            date = element.css(self.EXECUTIVE_DATE_CSS).extract_first()
            date = dateparser.parse(date, languages=["pt"]).date()
            pdf_title = element.css(self.EXECUTIVE_PDF_TEXT_CSS).extract_first()
            is_extra_edition = "Edição Extra" in pdf_title

            yield self.build_gazzete(date, url, "executive", is_extra_edition)

        steps = range(20, self.EXECUTIVE_LAST_PAGE, self.EXECUTIVE_STEP)
        for step in steps:
            url = self.EXECUTIVE_NEXT_PAGE_URL.format(step)
            yield Request(url, self.parse_executive)

    def parse_legislative(self, response):
        for element in response.css(self.LEGISLATIVE_GAZETTE_ROW_CSS):
            if not element.css("td"):
                continue

            url = element.css(self.LEGISLATIVE_PDF_HREF_CSS).extract_first()
            date = element.css(self.LEGISLATIVE_DATE_CSS)
            date = date.re(self.LEGISLATIVE_DATE_REGEX).pop()
            date = dateparser.parse(date, languages=["pt"]).date()

            yield self.build_gazzete(date, url, "legislative")

        for url in response.css(self.LEGISLATIVE_NEXT_PAGE_CSS).extract():
            yield Request(url, self.parse_legislative)

    def build_gazzete(self, date, url, power, is_extra_edition=False):
        return Gazette(
            date=date, file_urls=[url], is_extra_edition=is_extra_edition, power=power,
        )
