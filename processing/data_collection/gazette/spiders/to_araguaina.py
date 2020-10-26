from dateparser import parse
import requests
import re
import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider

only_number_regex = re.compile(r"\D*")


class ToAraguainaSpider(BaseGazetteSpider):
    TERRITORY_ID = "1702109"
    name = "to_araguaina"
    allowed_domains = [
        "diariooficial.araguaina.to.gov.br",
        "diariooficial.araguaina.tk",
    ]
    start_urls = ["http://diariooficial.araguaina.to.gov.br/Pesquisa/?De=05/12/2011"]

    def parse(self, response):
        rows = response.xpath('//table[@id="ContentPlaceHolder1_gvResultado"]/tbody/tr')
        for row in rows:
            is_extra_edition = False
            edition_number = row.xpath(".//td[1]/text()").extract_first().lower()
            edition_number = edition_number.strip()
            if "suplemento" in edition_number:
                edition_number = edition_number.split()[0]
                is_extra_edition = True
            edition_number = only_number_regex.sub("", edition_number)
            number_of_pages = row.xpath(".//td[3]/text()").extract_first()

            publication_date_str = row.xpath(".//td[2]/text()").extract_first()
            publication_date = parse(publication_date_str, languages=["pt"]).date()

            pdf_url = response.urljoin(row.xpath(".//td[6]/a/@href").extract_first())
            pdf_url = requests.head(pdf_url, allow_redirects=True).url
            gazette_object = self.create_gazette_object(
                date=publication_date,
                file_url=pdf_url,
                is_extra_edition=is_extra_edition,
            )

            yield gazette_object

    def create_gazette_object(
        self, date, file_url, is_extra_edition=False, power="executive"
    ):
        file_urls = [file_url]

        gazette_object = Gazette(
            date=date,
            file_urls=file_urls,
            is_extra_edition=is_extra_edition,
            power=power,
        )
        return gazette_object
