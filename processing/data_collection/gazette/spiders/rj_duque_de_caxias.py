import datetime as dt
import re

from dateparser import parse
import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class RjDuqueDeCaxiasSpider(BaseGazetteSpider):
    TERRITORY_ID = "3301702"
    name = "rj_duque_de_caxias"
    allowed_domains = ["duquedecaxias.rj.gov.br"]
    start_urls = ["http://duquedecaxias.rj.gov.br/portal/boletim-oficial.html"]

    def parse(self, response):
        current_year = dt.date.today().year

        pages = response.xpath("//center//div[1]//div//a/@href").extract()
        page_urls = [response.urljoin(url) for url in pages]

        years = response.xpath("//center//div[1]//div/text()").re("(\d{4})")

        self.parse_html_indexed_page(response, True, current_year)

        for year, url in zip(years, page_urls):
            yield scrapy.Request(url, callback=self.parse_page, meta={"year": year})

    def parse_page(self, response):
        year = response.meta["year"]
        if int(year) > 2016:
            self.parse_html_indexed_page(response, False, year)
        else:
            months = [
                "01-Janeiro",
                "02-Fevereiro",
                "03-Marco",
                "04-Abril",
                "05-Maio",
                "06-Junho",
                "07-Julho",
                "08-Agosto",
                "09-Setembro",
                "10-Outubro",
                "11-Novembro",
                "12-Dezembro",
            ]

            for month in months:
                url = response.urljoin(month)
                yield scrapy.Request(
                    url,
                    callback=self.parse_directory_page,
                    meta={"year": year, "month": month},
                )

    def parse_directory_page(self, response):
        month = response.meta["month"]
        year = response.meta["year"]
        pdf_names = response.xpath("//a/attribute::href").re("(.*).pdf")

        urls = [f"{response.urljoin(url)}.pdf" for url in pdf_names]

        dates = []
        for pdf in pdf_names:
            dat = f"{pdf[-2:]}/{month[:2]}/{year}"
            dates.append(parse(dat, languages=["pt"]).date())

        for url, date, name in zip(urls, dates, pdf_names):
            if "E" in name:
                is_extra_edition = True
            else:
                is_extra_edition = False

            yield Gazette(
                date=date,
                file_urls=[url],
                is_extra_edition=is_extra_edition,
                territory_id=self.TERRITORY_ID,
                power="executive_legislature",
                scraped_at=dt.datetime.utcnow(),
            )

    def parse_html_indexed_page(self, response, is_current_year, year):
        str_current = "//center/div[position()>1]"
        str_previous = "//center/div"

        if is_current_year:
            xpath = str_current
        else:
            xpath = str_previous

        urls_elems = response.xpath(f"{xpath}//a/@href").extract()

        urls = [response.urljoin(url) for url in urls_elems]

        full_dates = response.xpath(
            f"{xpath}//div[contains(text(), '{year}')]/text()"
        ).re("(\d{1,2}\s+de\s+\w+\s+\d{4})")

        dates = [parse(date, languages=["pt"]).date() for date in full_dates]

        names = response.xpath(
            f"{xpath}//div[contains(text(), 'Boletim ')]/text()"
        ).extract()

        for url, date, name in zip(urls, dates, names):
            if "Vol" in name or "Especial" in name:
                is_extra_edition = True
            else:
                is_extra_edition = False

            yield Gazette(
                date=date,
                file_urls=[url],
                is_extra_edition=is_extra_edition,
                territory_id=self.TERRITORY_ID,
                power="executive_legislature",
                scraped_at=dt.datetime.utcnow(),
            )
