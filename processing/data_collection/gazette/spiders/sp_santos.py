# -*- coding: utf-8 -*-
import datetime as dt

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class SpSantosSpider(BaseGazetteSpider):
    TERRITORY_ID = "3548500"
    name = "sp_santos"
    allowed_domains = ["santos.sp.gov.br"]
    start_urls = ["https://diariooficial.santos.sp.gov.br/"]
    download_url = "https://diariooficial.santos.sp.gov.br/edicoes/inicio/download/{}"

    def parse(self, response):
        # all of the dates with gazettes are available inside the following hidden textarea:
        dates = response.css("#datas.hidden::text").extract_first()

        start_date = dt.date(2015, 1, 1)
        parsing_date = dt.date.today()
        while parsing_date >= start_date:
            if str(parsing_date) in dates:
                url = self.download_url.format(parsing_date)
                yield Gazette(
                    date=parsing_date,
                    file_urls=[url],
                    is_extra_edition=False,
                    power="executive_legislature",
                )

            parsing_date = parsing_date - dt.timedelta(days=1)
