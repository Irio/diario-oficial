from dateparser import parse
import datetime as dt
from dateutil.rrule import rrule, MONTHLY

import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class SpGuarulhosSpider(BaseGazetteSpider):
    TERRITORY_ID = "3518800"
    name = "sp_guarulhos"
    allowed_domains = ["guarulhos.sp.gov.br"]

    def start_requests(self):
        starting_date = dt.date(2015, 1, 1)
        ending_date = dt.date.today()
        for date in rrule(MONTHLY, dtstart=starting_date, until=ending_date):
            yield scrapy.Request(
                f"http://www.guarulhos.sp.gov.br/diario-oficial/index.php?mes={date.month}&ano={date.year}"
            )

    def parse(self, response):
        diarios = response.xpath('//div[contains(@id, "diario")]')
        items = []
        for diario in diarios:
            date = diario.xpath(".//h3/text()").extract_first()
            date = parse(date[-10:], languages=["pt"]).date()
            is_extra_edition = False
            links = diario.xpath('.//a[contains(@href, ".pdf")]').xpath("@href")
            url = [response.urljoin(link) for link in links.extract()]
            power = "executive"
            items.append(
                Gazette(
                    date=date,
                    file_urls=url,
                    is_extra_edition=is_extra_edition,
                    power=power,
                )
            )
        return items
