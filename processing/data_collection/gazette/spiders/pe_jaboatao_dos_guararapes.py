from datetime import datetime

from dateparser import parse
from scrapy import Request

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class PeJaboataoDosGuararapesSpider(BaseGazetteSpider):
    TERRITORY_ID = "2607901"
    name = "pe_jaboatao_dos_guararapes"
    allowed_domains = ["diariooficial.jaboatao.pe.gov.br"]
    start_urls = ["https://diariooficial.jaboatao.pe.gov.br/"]

    def parse(self, response):
        for gazette_card in response.css(".elementor-post__card"):
            yield Request(
                gazette_card.css(".elementor-post__title a::attr(href)").get(),
                callback=self.parse_gazette_page,
                meta={
                    "date": parse(
                        gazette_card.css(".elementor-post-date::text").get(),
                        languages=["pt"],
                    ),
                },
            )

        next_page = response.css("a.next::attr(href)").get()
        if next_page:
            yield Request(next_page)

    def parse_gazette_page(self, response):
        pdf_link = response.css(".dkpdf-button::attr(href)").get()
        file_url = response.urljoin(pdf_link)

        return Gazette(
            date=response.meta["date"],
            file_urls=[file_url],
            is_extra_edition="edicao-extraordinaria" in file_url,
            territory_id=self.TERRITORY_ID,
            power="executive",
            scraped_at=datetime.utcnow(),
        )
