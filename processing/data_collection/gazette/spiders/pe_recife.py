"""Recife's gazettes spider

This spider is implemented to crawl Recife's `newest gazette system
<https://www.cepe.com.br/>`_. This system covers gazettes from 30/04/2015 to
current days. There is also a `deprecated system
<http://www.recife.pe.gov.br/diariooficial-acervo/>`_ which covers gazettes from 2001
to 2016 which is still not implemented.

Implementation details:
    The spider generates all dates from the first available date (30/04/2015) until
    today. These dates are used to fetch the name of all available gazettes on that
    date, including Recife's. Then, the respective documents for Recife's gazettes
    are requested and the rest if filtered out.

Gazettes examples:
    - http://200.238.105.211/cadernos/2020/20200326/8-PrefeituradoRecifeEdicaoExtra/PrefeituradoRecifeEdicaoExtra(20200326).pdf
    - http://200.238.105.211/cadernos/2020/20200613/8-PrefeituradoRecife/PrefeituradoRecife(20200613).pdf
    - http://200.238.105.211/cadernos/2020/20200616/8-PrefeituradoRecife/PrefeituradoRecife(20200616).pdf

"""

import datetime as dt
import re

import dateparser
from dateutil.rrule import DAILY, rrule
import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class PeRecifeSpider(BaseGazetteSpider):
    name = "pe_recife"
    TERRITORY_ID = "2611606"

    FIRST_AVAILABLE_DATE = dt.date(2015, 4, 30)

    AVAILABLE_DATES_URL = "https://ws.cepe.com.br/publicar/dows.php"
    EDITIONS_IN_DATE_URL = "https://ws.cepe.com.br/publicar/dows.php?&dia={full_date}"
    GAZETTE_URL = "http://200.238.105.211/cadernos/{full_year}/{full_date}/{edition_type}/{edition_type_name_only}({full_date}).pdf"

    def start_requests(self):
        """
        Requests documents which specifies edition types available for dates.
        """
        dates = rrule(
            freq=DAILY, dtstart=self.FIRST_AVAILABLE_DATE, until=dt.date.today()
        )

        for date in dates:
            yield scrapy.Request(
                url=self.EDITIONS_IN_DATE_URL.format(full_date=date.strftime("%Y%m%d")),
                meta={"date": date},
                callback=self.parse_editions_in_date,
            )

    def parse_editions_in_date(self, response):
        """
        Parses available editions to request only Recife's gazette documents.
        """
        recife_editions = self._find_recife_editions(response.text)
        date = response.meta["date"]

        for edition in recife_editions:
            url = self.GAZETTE_URL.format(
                full_year=date.strftime("%Y"),
                full_date=date.strftime("%Y%m%d"),
                edition_type=edition,
                edition_type_name_only=re.search("\w+$", edition).group(),
            )

            yield Gazette(
                date=date,
                file_urls=[url],
                is_extra_edition=self._is_extra(edition),
                power="executive_legislative",
            )

    def _find_recife_editions(self, text):
        """
        Finds editions related to Recife's gazette.

        Filters out entries which are not exclusively related to Recife
        (e.g. "1-PoderExecutivo").
        """
        return (
            edition
            for edition in text.split("&")
            if re.search("prefeituradorecife", edition, re.IGNORECASE)
        )

    def _is_extra(self, edition):
        """
        Checks if edition is extra or not.
        """
        return re.search("extra", edition, re.IGNORECASE) is not None
