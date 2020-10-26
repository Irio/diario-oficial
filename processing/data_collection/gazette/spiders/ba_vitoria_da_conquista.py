from datetime import date
from dateparser import parse

import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class BaVitoriaDaConquistaSpider(BaseGazetteSpider):
    TERRITORY_ID = "2933307"
    name = "ba_vitoria_da_conquista"
    allowed_domains = ["pmvc.ba.gov.br"]
    start_urls = ["https://dom.pmvc.ba.gov.br/"]

    def start_requests(self):
        url = "https://dom.pmvc.ba.gov.br/diarios/{year}/{month}"
        for year in range(2013, date.today().year + 1):
            for month in range(1, 13):
                yield scrapy.Request(url.format(year=year, month=month))

    def parse(self, response):
        """
        Extracts the gazette items from the web page.
        """
        boxes = response.css(".box-diario")
        links_xpath = './/a[text()[normalize-space(.) = "Visualizar Diário"]]/@href'
        for box in boxes:
            parsing_date = box.re("diario-(\d{8})")[0]
            parsing_date = parse(parsing_date, date_formats=["%Y%m%d"]).date()
            url = box.xpath(links_xpath).extract_first()
            url = url.replace("previsualizar", "baixar")
            yield Gazette(
                date=parsing_date,
                file_urls=[url],
                is_extra_edition=False,
                power="executive_legislature",
            )
