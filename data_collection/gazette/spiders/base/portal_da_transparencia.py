import datetime

import dateparser
from scrapy import Request

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class PortalDaTransparenciaBaseSpider(BaseGazetteSpider):
    allowed_domains = ["portaldatransparencia.com.br"]
    start_date = datetime.date(2000, 1, 1)

    def parse(self, response):
        for issue in response.css("div.box-edicao"):
            date = self.get_issue_date(issue)
            if date < self.start_date:
                return

            gazette_file_url = response.urljoin(
                issue.css("a.btn_visualizar::attr(href)").get()
            )

            edition_number, is_extra_edition = self.get_edition_number(issue)

            yield Gazette(
                date=date,
                file_urls=[gazette_file_url],
                is_extra_edition=is_extra_edition,
                edition_number=edition_number,
                power="executive",
            )

        next_page_url = response.urljoin(response.css("a.proximo::attr(href)").get())

        if next_page_url:
            yield Request(next_page_url)

    def get_issue_date(self, issue):
        issue_date = issue.css("div.data-caderno ::text").get()
        return dateparser.parse(issue_date, languages=["pt"]).date()

    def get_edition_number(self, issue):
        edition_element = issue.css("span.edicao > strong ::text")
        edition_number = edition_element.re_first(r"Edição (\d+)")
        is_extra_edition = "Caderno 1" not in edition_element.get()
        return edition_number, is_extra_edition
