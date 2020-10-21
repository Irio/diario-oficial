import dateparser
from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class MgContagemSpider(BaseGazetteSpider):
    TERRITORY_ID = "3118601"
    name = "mg_contagem"
    allowed_domains = ["contagem.mg.gov.br"]
    start_urls = ["http://www.contagem.mg.gov.br/?se=doc"]

    def parse(self, response):
        """
        @url http://www.contagem.mg.gov.br/?se=doc&pagina=2
        @returns items 15 15
        @scrapes date file_urls is_extra_edition power
        """
        anchor_elements = response.css(".texto11pt a")

        urls = [
            response.urljoin(url)
            for url in anchor_elements.css("::attr(href)").re(".+pdf")
        ]
        extra_editions = ["complementar" in url for url in urls]

        dates_in_sentence = anchor_elements.css("p span:last-child ::text").re(
            "(\d{1,2}\s+de\s+\w+\s+de\s+\d{4})"
        )
        dates = [
            dateparser.parse(date, languages=["pt"]).date()
            for date in dates_in_sentence
        ]

        for url, date, is_extra_edition in zip(urls, dates, extra_editions):
            yield Gazette(
                date=date,
                file_urls=[url],
                is_extra_edition=is_extra_edition,
                power="executive_legislature",
            )

        number_of_pages = int(
            response.css("table.subtitulo12pt tr:first-child td ::text").extract()[-1]
        )
        for next_page in range(2, number_of_pages + 1):
            next_page_url = f"{self.start_urls[0]}&pagina={next_page}"
            yield response.follow(next_page_url, callback=self.parse)
