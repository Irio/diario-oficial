import json
import time
import datetime

from scrapy import Request
from dateutil.rrule import rrule, MONTHLY
from dateparser import parse

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


BASE_URL = "http://gazetamunicipal.cuiaba.mt.gov.br/api/api/editions"


class MtCuiabaSpider(BaseGazetteSpider):
    TERRITORY_ID = "5103403"
    name = "mt_cuiaba"
    allowed_domains = ["gazetamunicipal.cuiaba.mt.gov.br"]
    start_urls = ["http://gazetamunicipal.cuiaba.mt.gov.br/"]

    custom_settings = {
        "DOWNLOAD_DELAY": 1,
    }

    def start_requests(self):
        start_date = datetime.date(1967, 1, 1)
        end_date = datetime.date.today()

        for date in rrule(MONTHLY, dtstart=start_date, until=end_date):
            date_url = f"{BASE_URL}/published/{date.year}/{date.month}"
            yield Request(
                url=date_url,
                headers={"referer": "https://diariooficial.cuiaba.mt.gov.br/edicoes",},
            )

    def parse(self, response):
        editions = json.loads(response.text)["editions"]
        for edition in editions:
            edition_id = edition["id"]
            edition_url = f"{BASE_URL}/downloadPdf/{edition_id}"
            edition_date = edition["publication_date"]

            yield Gazette(
                date=parse(edition_date, languages=["pt"]),
                file_urls=[edition_url],
                is_extra_edition=edition["suplement"],
                territory_id=self.TERRITORY_ID,
                power="executive",
                scraped_at=datetime.datetime.utcnow(),
            )
