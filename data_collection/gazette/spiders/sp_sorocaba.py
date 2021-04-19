import re
from datetime import date, datetime

from scrapy import Request
from dateparser import parse
from dateutil.rrule import MONTHLY, rrule

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class SpSorocabaSpider(BaseGazetteSpider):
    name = "sp_sorocaba"
    TERRITORY_ID = "3552205"

    start_date = date(2005, 1, 7)

    gazettes_list_url = "http://noticias.sorocaba.sp.gov.br/jornal/?ano={}"

    MonthDict = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Marco",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro",
    }

    def start_requests(self):
        end_date = date.today()

        periods_of_interest = [
            (date.year, date.month)
            for date in rrule(freq=MONTHLY, dtstart=self.start_date, until=end_date)
        ]
        global year
        for year, month_int in periods_of_interest:
            month_text = self.MonthDict[month_int]
            period = f"{ year }+{ month_text }"
            url = self.gazettes_list_url.format(period)
            yield Request(url, self.parse)

    def parse(self, response):
        for link in response.css("div.list-group-flush.w-100 a::attr(href)"):
            url = self.get_pdf_url(response, link)
            if not url:
                continue

            [gazette_date, gazette_edition_number] = self.get_date_and_edition_number(
                link
            )

            yield Gazette(
                date=gazette_date,
                edition_number=gazette_edition_number,
                file_urls=(url,),
                is_extra_edition=False,
                territory_id=self.TERRITORY_ID,
                power="executive_legislature",
                scraped_at=datetime.utcnow(),
            )

        next_page = response.css("li.next.page-item a::attr(href)").extract()
		
		if next_page:
            yield Request(next_page[0], dont_filter=True)

    @staticmethod
    def get_pdf_url(response, link):
        relative_url = link.get()

        if not relative_url.lower().endswith(".pdf"):
            return None

        return response.urljoin(relative_url)

    @staticmethod
    def get_date_and_edition_number(link):
        pattern = r"\d+.\d{1,}-\d{1,2}-de-\w+"
        match_edition_number_day_month = re.search(pattern, link.get())

        if not match_edition_number_day_month:
            return [None, None]

        [edition_number, date_raw] = match_edition_number_day_month.group().split(
            "-", 1
        )
        date_raw_with_spaces = date_raw.replace("-", " ")
        date_raw_with_spaces_year = date_raw_with_spaces + f" de { year }"

        return [
            parse(date_raw_with_spaces_year, languages=("pt",)).date(),
            edition_number,
        ]