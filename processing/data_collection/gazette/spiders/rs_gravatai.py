from dateparser import parse

from scrapy import Request

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class RsGravataiSpider(BaseGazetteSpider):
    TERRITORY_ID = "4309209"
    name = "rs_gravatai"
    allowed_domains = ["gravatai.atende.net"]
    start_urls = ["https://gravatai.atende.net/?pg=diariooficial"]

    extra_editions_options = ("Suplementar", "Retificação")

    def parse(self, response):
        """
        @url https://gravatai.atende.net/?pg=diariooficial
        @returns requests 1
        """

        last_page_number_css = "#paginacao > ul > li:nth-child(7) > button::attr(value)"
        last_page_number = int(response.css(last_page_number_css).extract_first())

        for page_number in range(1, last_page_number + 1):
            yield Request(
                f"https://gravatai.atende.net/?pg=diariooficial&pagina={page_number}",
                callback=self.parse_gazette,
            )

    def parse_gazette(self, response):
        """
        @url https://gravatai.atende.net/?pg=diariooficial&pagina=1
        @returns items 1
        @scrapes date file_urls is_extra_edition power
        """

        for element in response.css(".nova_listagem > .linha"):
            info = element.css(".info")

            is_extra_edition = (
                info.css(".tipo::text").extract_first() in self.extra_editions_options
            )

            date = parse(
                info.css(".data::text").extract_first(), languages=["pt"]
            ).date()

            code = element.css(".opcoes > button::attr(data-codigo)").extract_first()
            url = (
                "https://gravatai.atende.net/atende.php?rot=54002&aca=737"
                f"&processo=download&codigo={code}"
            )

            yield Gazette(
                date=date,
                file_urls=[url],
                is_extra_edition=is_extra_edition,
                power="executive",
            )
