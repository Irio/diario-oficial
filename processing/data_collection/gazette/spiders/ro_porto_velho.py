import datetime as dt
import json

from dateutil.rrule import rrule, MONTHLY
from dateparser import parse
from scrapy.http import Request
from scrapy.selector import Selector

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class RoPortoVelho(BaseGazetteSpider):
    TERRITORY_ID = "1100205"
    BASE_URL = "https://www.portovelho.ro.gov.br/dom/datatablearquivosmes/"
    AVAILABLE_FROM = dt.datetime(2007, 1, 1)

    name = "ro_porto_velho"
    allowed_domains = ["portovelho.ro.gov.br"]

    def start_requests(self):
        interval = rrule(MONTHLY, dtstart=self.AVAILABLE_FROM, until=dt.date.today())[
            ::-1
        ]
        for date in interval:
            yield Request(f"{self.BASE_URL}{date.year}/{date.month}")

    def parse(self, response):
        paragraphs = json.loads(response.body_as_unicode())["aaData"]
        for paragraph, *_ in paragraphs:
            selector = Selector(text=paragraph)
            url = selector.css("p a ::attr(href)").extract_first()

            text = selector.css("p strong ::text")
            is_extra_edition = text.extract_first().startswith("Suplemento")
            date = text.re_first("\d{1,2} de \w+ de \d{4}")
            date = parse(date, languages=["pt"]).date()

            yield Gazette(
                date=date,
                file_urls=[url],
                is_extra_edition=is_extra_edition,
                power="executive_legislature",
            )
