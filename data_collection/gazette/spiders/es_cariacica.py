import datetime
import re
from urllib.parse import urlencode

from dateutil.rrule import WEEKLY, rrule
from scrapy.http import Request

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class EsCariacicaSpider(BaseGazetteSpider):
    name = "es_cariacica"
    TERRITORY_ID = "3201308"
    start_urls = ["https://www.cariacica.es.gov.br/publicacoes/diario-oficial/"]
    start_date = datetime.date(2014, 7, 1)
    end_date = datetime.date.today()

    def parse(self, response):
        search_period = rrule(freq=WEEKLY, dtstart=self.start_date, until=self.end_date)

        for date in search_period:
            start = date.strftime("%Y-%m-%d")
            last_day = date + datetime.timedelta(days=6)
            end = last_day.strftime("%Y-%m-%d")
            interval = {"inicio": start, "fim": end}
            link = f"{self.start_urls[0]}?{urlencode(interval)}"
            yield Request(url=link, callback=self.parse_week)

    def parse_week(self, response):
        date_cards = response.css("div.card div.card-header")

        for card in date_cards[1:]:
            date = card.xpath("./b/text()").get()
            date = datetime.datetime.strptime(date, "%d/%m/%Y").date()

            gazettes = card.xpath("./following-sibling::table/tr")
            for gazette in gazettes[1:]:
                link = gazette.xpath("./td[4]/a/@href").get()
                title = gazette.xpath("./td[1]/text()").get()
                extra_edition = "extra" in title.lower()
                edition = re.search(r"EDIÇÃO N.+?(\d+)", title)
                edition = edition.group(1) if edition is not None else ""

                yield Gazette(
                    date=date,
                    file_urls=[response.urljoin(link)],
                    is_extra_edition=extra_edition,
                    edition_number=edition,
                    power="executive_legislative",
                )
