from datetime import datetime

import dateparser

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class PbJoaoPessoaSpider(BaseGazetteSpider):
    TERRITORY_ID = "2507507"

    EXTRA_EDITION_CSS = "td:first-child"
    GAZETTE_ROW_CSS = ".table-semanarios table tbody tr"
    GAZETTE_URL_CSS = "td:last-child a::attr(href)"
    NEXT_PAGE_CSS = ".pagination a.next::attr(href)"
    DATE_CSS = "td:nth-last-child(2)::text"
    DATE_REGEX = r"[0-9]{2}/[0-9]{2}/[0-9]{4}"

    name = "pb_joao_pessoa"
    start_urls = ["http://antigo.joaopessoa.pb.gov.br/semanariooficial/"]

    def parse(self, response):
        """Parses gazettes page and requests next page.

        Normal gazettes are displayed in a weekly basis, so, the date which is taken
        into account for this type of gazette is the last in the publication period
        (i.e. "29/08/2020" from "23/08/2020 to 29/08/2020").

        Special gazzetes are daily, but that same logic applies here and it works
        correctly.
        """

        for element in response.css(self.GAZETTE_ROW_CSS):
            url = element.css(self.GAZETTE_URL_CSS).extract_first()
            date = element.css(self.DATE_CSS).re(self.DATE_REGEX).pop()
            date = dateparser.parse(date, languages=["pt"]).date()
            is_extra = "Especial" in element.css(self.EXTRA_EDITION_CSS).extract_first()

            yield Gazette(
                date=date,
                file_urls=[url],
                is_extra_edition=is_extra,
                territory_id=self.TERRITORY_ID,
                power="executive_legislature",
                scraped_at=datetime.utcnow(),
            )

        for url in response.css(self.NEXT_PAGE_CSS).extract():
            yield response.follow(url)
