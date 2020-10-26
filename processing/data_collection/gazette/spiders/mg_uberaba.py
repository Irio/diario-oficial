import re
import datetime as dt

from dateparser import parse
from scrapy.http import FormRequest

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class MgUberaba(BaseGazetteSpider):
    TERRITORY_ID = "3170107"
    name = "mg_uberaba"
    allowed_domains = ["uberaba.mg.gov.br"]

    LIST_GAZETTES_URL = "http://www.uberaba.mg.gov.br/portal/listImagesHtml"
    DOWNLOAD_URL_TEMPLATE = (
        "http://www.uberaba.mg.gov.br:8080/portal/acervo/portavoz/arquivos/{}/{}"
    )

    def start_requests(self):
        next_year = dt.datetime.today().year + 1

        for year in range(2015, next_year):
            yield FormRequest(
                url=self.LIST_GAZETTES_URL,
                method="POST",
                formdata={
                    "desc": "1",
                    "type": "1",
                    "folder": f"portavoz/arquivos/{year}",
                    "limit": "5000",
                    "page": "1",
                    "types": "pdf",
                    "listAll": "1",
                },
                meta={"year": year},
            )

    def parse(self, response):
        filenames = [
            filename.strip()
            for filename in response.xpath(
                '//div[@class="claGaleriaBoxFileTable"]/text()'
            ).extract()
        ]
        for filename in filenames:
            date = self.extract_date(filename)
            yield Gazette(
                date=date,
                file_urls=[self.mount_url(filename, date.year)],
                is_extra_edition=False,
                power="executive_legislature",
            )

    def extract_date(self, filename):
        date_str = re.search(r"(\d{2}-\d{2}-\d{4})", filename).group(1)
        return parse(date_str, languages=["pt"]).date()

    def mount_url(self, filename, year):
        return self.DOWNLOAD_URL_TEMPLATE.format(year, filename)
