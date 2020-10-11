import dateparser
from datetime import datetime, date
from urllib.parse import unquote
from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider
from scrapy import FormRequest, Request
from scrapy.selector.unified import Selector
from gazette.settings import FILES_STORE
import re
from w3lib.html import remove_tags
from pathlib import Path
from typing import Optional
from hashlib import sha1
from fake_useragent import UserAgent


class SpSantoAndreSpider(BaseGazetteSpider):
    name = "sp_santo_andre"
    TERRITORY_ID = "3547809"
    custom_settings = {
        "ITEM_PIPELINES": {
            "gazette.pipelines.GazetteDateFilteringPipeline": 50,
            "gazette.pipelines.ExtractTextPipeline": 200,
        },
        "USER_AGENT": UserAgent().random,
    }

    allowed_domains = ["santoandre.sp.gov.br"]
    start_urls = [
        "http://www.santoandre.sp.gov.br/publicacao/edicao/consultaedicao.aspx"
    ]
    start_date = date(2010, 1, 1)
    TODAY = datetime.now().strftime("%d/%m/%Y")
    JAVASCRIPT_POSTBACK_REGEX = r"javascript:__doPostBack\('(.*)',''\)"
    CURRENT_PAGE = 1

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, callback=self.search_by_date)

    def search_by_date(self, response):
        yield FormRequest.from_response(
            response,
            callback=self.parse,
            formname="aspnetForm",
            formdata={
                "ctl00$ContentPlaceHolder1$dt_inicio": self.start_date.strftime(
                    "%d/%m/%Y"
                ),
                "ctl00$ContentPlaceHolder1$dt_final": self.TODAY,
            },
            clickdata={"name": "ctl00$ContentPlaceHolder1$PsaToolBar1$btnSelecionar"},
            method="POST",
        )

    def _save_pdf(self, response, path, item):
        if not isinstance(path, Path):
            raise TypeError("The path parameter must be an instance of Path.")
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "wb") as f:
            f.write(response.body)
        yield item

    def _parse_table_elements(self, element):
        if not isinstance(element, Selector):
            raise TypeError("The parameter element must be a Selector instance.")
        doPostBack, num_edicao, date = element.xpath(".//td").getall()
        event_target = unquote(
            re.search(self.JAVASCRIPT_POSTBACK_REGEX, doPostBack).groups()[0]
        )
        num_edicao = remove_tags(num_edicao)
        date = dateparser.parse(remove_tags(date), languages=["pt"]).date()

        return event_target, num_edicao, date

    def _format_filename(self, num_edicao, event_target, date):
        filename = sha1(
            str.encode(
                f"{self.allowed_domains[0].replace('.','')}-{event_target}-{num_edicao}-{date}"
            )
        ).hexdigest()
        filename = f"{filename}.pdf"
        file_path = Path(f"{FILES_STORE}full/{filename}")
        return file_path

    def _handle_navigation(self, response, current_page):
        """Identifies the elements for pagination.
        Parameters
        ----------
        current_page : int
            The current page number of the pagination
        Returns : str or None
        -------
            If there is a pagination to follow, this function will return the __EVENTTARGET parameter, otherwise, will return None.
        """
        next_page_element = (
            response.css(".DataGrid")
            .xpath(".//*[contains(@class, 'DataGridPager')]//a")
            .getall()
        )
        for index, element in enumerate(next_page_element):
            try:
                filter_next_page = int(remove_tags(element))
            except ValueError:
                filter_next_page = remove_tags(element)
            finally:
                if filter_next_page == current_page + 1:
                    self.CURRENT_PAGE += 1
                    event_target = unquote(
                        re.search(self.JAVASCRIPT_POSTBACK_REGEX, element).groups()[0]
                    )
                    return event_target
                if filter_next_page == "..." and index != 0:
                    self.CURRENT_PAGE += 1
                    event_target = unquote(
                        re.search(self.JAVASCRIPT_POSTBACK_REGEX, element).groups()[0]
                    )
                    return event_target
        return None

    def parse(self, response):
        records = response.css(".DataGrid").xpath(
            ".//*[contains(@class, 'DataGridItems')] | .//*[contains(@class, 'DataGridAlternating')]"
        )
        for element in records:
            EVENT_TARGET, num_edicao, date = self._parse_table_elements(element)
            file_path = self._format_filename(num_edicao, EVENT_TARGET, date)
            item = Gazette(
                date=date,
                is_extra_edition=False,
                territory_id=self.TERRITORY_ID,
                power="executive_legislature",
                scraped_at=datetime.utcnow(),
                files=[{"path": str(file_path)}],
            )
            yield FormRequest.from_response(
                response,
                callback=self._save_pdf,
                cb_kwargs=dict(path=file_path, item=item),
                formname="aspnetForm",
                formdata={
                    "__EVENTTARGET": EVENT_TARGET,
                    "ctl00$ContentPlaceHolder1$dt_inicio": self.start_date.strftime(
                        "%d/%m/%Y"
                    ),
                    "ctl00$ContentPlaceHolder1$dt_final": self.TODAY,
                },
                method="POST",
                dont_click=True,
                dont_filter=True,
            )
        event_target = self._handle_navigation(response, current_page=self.CURRENT_PAGE)
        if event_target:
            yield FormRequest.from_response(
                response,
                callback=self.parse,
                formname="aspnetForm",
                formdata={
                    "__EVENTTARGET": event_target,
                    "ctl00$ContentPlaceHolder1$dt_inicio": self.start_date.strftime(
                        "%d/%m/%Y"
                    ),
                    "ctl00$ContentPlaceHolder1$dt_final": self.TODAY,
                },
                clickdata={
                    "name": "ctl00$ContentPlaceHolder1$PsaToolBar1$btnSelecionar"
                },
                method="POST",
                dont_click=True,
                dont_filter=True,
            )
