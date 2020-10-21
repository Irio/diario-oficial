import dateparser

from scrapy import Request, Spider
from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class ScJoinvilleSpider(BaseGazetteSpider):
    TERRITORY_ID = "4209102"
    PDF_URL = "https://www.joinville.sc.gov.br{}"

    GAZETTE_ELEMENT_CSS = "ul.jornal li"
    NEXT_PAGE_CSS = "ul.pagination li.next a::attr(href)"
    DATE_CSS = "span.article-date::text"
    EXTRA_EDITION_CSS = "span.edicao_extraordinaria::text"
    DATE_REGEX = "([\d]+)[ |]+([\w]+)[ |]+([\d]+)"

    allowed_domains = ["joinville.sc.gov.br"]
    name = "sc_joinville"
    start_urls = ["https://www.joinville.sc.gov.br/jornal/index/page/1"]

    def parse(self, response):
        """
        @url http://www.joinville.sc.gov.br/jornal/index/page/1
        @returns requests 1
        @scrapes date file_urls is_extra_edition power
        """

        for element in response.css(self.GAZETTE_ELEMENT_CSS):
            date = self.extract_date(element)
            url = self.extract_url(element)
            is_extra_edition = self.extract_extra_edition_info(element)

            yield Gazette(
                date=date,
                file_urls=[url],
                is_extra_edition=is_extra_edition,
                power="executive_legislature",
            )

        for url in response.css(self.NEXT_PAGE_CSS).extract():
            yield Request(url)

    def extract_date(self, element):
        date = element.css(self.DATE_CSS).re(self.DATE_REGEX)
        date = "/".join(date)
        return dateparser.parse(date, languages=["pt"]).date()

    def extract_url(self, element):
        path = element.css("a::attr(href)").extract_first()
        return self.PDF_URL.format(path)

    def extract_extra_edition_info(self, element):
        extra_edition_data = element.css(self.EXTRA_EDITION_CSS).extract_first()
        return extra_edition_data == "Edição Extraordinária"
