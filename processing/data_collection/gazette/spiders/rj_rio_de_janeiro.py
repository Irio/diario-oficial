import datetime

import scrapy
from dateutil.rrule import DAILY, rrule

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class RjRioDeJaneiroSpider(BaseGazetteSpider):
    TERRITORY_ID = "3304557"
    name = "rj_rio_de_janeiro"
    allowed_domains = ["doweb.rio.rj.gov.br"]

    start_date = datetime.date(2006, 3, 16)

    def start_requests(self):
        for date in rrule(
            freq=DAILY, dtstart=self.start_date, until=datetime.date.today()
        ):
            day = str(date.day).zfill(2)
            month = str(date.month).zfill(2)
            url = f"https://doweb.rio.rj.gov.br/apifront/portal/edicoes/edicoes_from_data/{date.year}-{month}-{day}.json"
            yield scrapy.Request(url=url, cb_kwargs={"gazette_date": date.date()})

    def parse(self, response, gazette_date):
        gazette_data = response.json()
        if gazette_data["erro"]:
            return

        items = gazette_data.get("itens", [])
        for item in items:
            gazette_id = item["id"]
            gazette_url = (
                f"https://doweb.rio.rj.gov.br/portal/edicoes/download/{gazette_id}"
            )
            is_extra_edition = item["suplemento"] == 1
            yield Gazette(
                date=gazette_date,
                file_urls=[gazette_url],
                is_extra_edition=is_extra_edition,
                territory_id=self.TERRITORY_ID,
                power="executive",
                scraped_at=datetime.datetime.utcnow(),
            )
