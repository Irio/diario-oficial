import datetime

from gazette.spiders.base import BaseGazetteSpider
from gazette.items import Gazette


class RjSaoGoncaloSpider(BaseGazetteSpider):
    TERRITORY_ID = "3304904"
    DOWNLOAD_GAZETTE_URL = "https://servicos.pmsg.rj.gov.br/diario/{}.pdf"
    start_date = datetime.date(1998, 2, 3)

    name = "rj_sao_goncalo"
    allowed_domains = ["servicos.pmsg.rj.gov.br"]
    start_urls = ["https://servicos.pmsg.rj.gov.br/diario_oficial.php"]

    def parse(self, response):
        date = datetime.date.today()
        start_date = self.start_date
        while date >= start_date:
            is_weekend = date.weekday() >= 5
            if is_weekend:
                date = date - datetime.timedelta(days=1)
                continue

            url = self.DOWNLOAD_GAZETTE_URL.format(date.strftime("%Y_%m_%d"))
            # TODO: How to figure out is_extra_edition? Doesn't seem possible
            # without extracting the text.
            yield Gazette(
                date=date,
                file_urls=[url],
                territory_id=self.TERRITORY_ID,
                power="executive",
                scraped_at=datetime.datetime.utcnow(),
            )
            date = date - datetime.timedelta(days=1)
