import datetime

import scrapy
from dateutil.rrule import MONTHLY, rrule

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class MsCampoGrandeSpider(BaseGazetteSpider):
    TERRITORY_ID = "5002704"
    name = "ms_campo_grande"
    allowed_domains = ["portal.capital.ms.gov.br"]
    start_date = datetime.date(1998, 1, 9)  # First gazette available

    def start_requests(self):
        periods_of_interest = [
            (str(date.year), str(date.month).zfill(2))
            for date in rrule(
                freq=MONTHLY, dtstart=self.start_date, until=datetime.date.today()
            )
        ]
        for year, month in periods_of_interest:
            yield scrapy.FormRequest(
                "http://portal.capital.ms.gov.br/diogrande/diarioOficial",
                formdata={"mes": month, "ano": year,},
                cb_kwargs={"month": month, "year": year},
            )

    def parse(self, response, month, year):
        gazettes = response.css(".arquivos li")
        for gazette in gazettes:
            day = gazette.css(".day strong::text").get()
            gazette_date = datetime.datetime.strptime(
                f"{year}-{month}-{day}", "%Y-%m-%d"
            ).date()

            gazette_url = gazette.css("a::attr(href)").get()
            is_extra_edition = bool(gazette.css("p::text").re(r"Extra|Suplemento"))

            yield Gazette(
                date=gazette_date,
                file_urls=[gazette_url],
                is_extra_edition=is_extra_edition,
                territory_id=self.TERRITORY_ID,
                power="executive_legislature",
                scraped_at=datetime.datetime.utcnow(),
            )
