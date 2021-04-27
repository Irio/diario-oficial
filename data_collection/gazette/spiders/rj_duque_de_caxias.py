from datetime import date

import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class RjDuqueDeCaxiasSpider(BaseGazetteSpider):
    TERRITORY_ID = "3301702"
    name = "rj_duque_de_caxias"
    allowed_domains = ["duquedecaxias.rj.gov.br"]
    start_urls = ["https://duquedecaxias.rj.gov.br"]
    base_url = "https://duquedecaxias.rj.gov.br/portal"
    base_url_before_2017 = base_url + "/boletim-oficial/{}/{}"
    base_url_after_2017 = base_url + "/{}.html"
    start_date = date(2013, 1, 1)

    month_names = [
        "Janeiro",
        "Fevereiro",
        "Marco",
        "Abril",
        "Maio",
        "Junho",
        "Julho",
        "Agosto",
        "Setembro",
        "Outubro",
        "Novembro",
        "Dezembro",
    ]

    def start_requests(self):
        end_date = date.today()
        year = self.start_date.year
        while year <= end_date.year:
            month = self.start_date.month
            while month < len(self.month_names):
                if year < 2017:
                    url = self.base_url_before_2017.format(
                        year, "{:02d}".format(month + 1) + "-" + self.month_names[month]
                    )
                else:
                    url = self.base_url_after_2017.format(year)
                yield scrapy.Request(url)
                month += 1
            year += 1

    def parse(self, response):
        for element in response.xpath('//a[contains(@href,"pdf")]/@href'):
            if ".html" in response.url:
                url = self.base_url + element.get()
            else:
                url = response.url + element.get()
            extra_edition = False
            if element.get().lower() in "extraordionario":
                extra_edition: True
            gazette_date = date.today()
            yield Gazette(
                date=gazette_date,
                file_urls=[url],
                is_extra_edition=extra_edition,
                power="executive_legislative",
            )
