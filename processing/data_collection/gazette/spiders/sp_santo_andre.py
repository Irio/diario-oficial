import dateparser
from datetime import datetime
from urllib.parse import unquote
from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider
from scrapy import FormRequest, Request
from scrapy.selector.unified import Selector
from gazette.settings import FILES_STORE
import re
from w3lib.html import remove_tags
from pathlib import Path


class SpSantoAndreSpider(BaseGazetteSpider):
    name = "sp_santo_andre"
    TERRITORY_ID = "3547809"
    custom_settings = {
        "ITEM_PIPELINES": {
            "gazette.pipelines.GazetteDateFilteringPipeline": 50,
            "gazette.pipelines.ExtractTextPipeline": 200,
        }
    }

    allowed_domains = ["santoandre.sp.gov.br"]
    start_urls = [
        "http://www.santoandre.sp.gov.br/publicacao/edicao/consultaedicao.aspx"
    ]
    # TODAY = datetime.now().strftime("%d/%m/%Y")
    JAVASCRIPT_POSTBACK_REGEX = r"javascript:__doPostBack\('(.*)',''\)"

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, callback=self.search_by_date)

    def _get_form_params(self, response):
        view_state = response.css("#__VIEWSTATE::attr(value)").get()
        event_validation = response.css("#__EVENTVALIDATION::attr(value)").get()
        return view_state, event_validation

    def search_by_date(self, response):
        VIEW_STATE, EVENT_VALIDATION = self._get_form_params(response)
        yield FormRequest.from_response(
            response,
            callback=self.parse,
            formname="aspnetForm",
            formdata={
                "__EVENTTARGET": "",
                "__EVENTARGUMENT": "",
                "__VIEWSTATE": VIEW_STATE,
                "__EVENTVALIDATION": EVENT_VALIDATION,
                "ctl00$ContentPlaceHolder1$dt_inicio": "01/01/2010",
                # "ctl00$ContentPlaceHolder1$dt_final": self.TODAY,
                "ctl00$ContentPlaceHolder1$dt_final": "31/01/2010",
            },
            clickdata={"name": "ctl00$ContentPlaceHolder1$PsaToolBar1$btnSelecionar"},
            method="POST",
        )

    def _save_pdf(self, response, path: Path, item):
        if not isinstance(path, Path):
            raise TypeError("O parâmetro path precisa ser uma instância de Path.")
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "wb") as f:
            f.write(response.body)
        yield item

    def _parse_table_elements(self, element: Selector):
        if not isinstance(element, Selector):
            raise TypeError("O parâmetro element deve ser uma instancia de Selector.")
        doPostBack, num_edicao, date = element.xpath(".//td").getall()
        event_target = unquote(
            re.search(self.JAVASCRIPT_POSTBACK_REGEX, doPostBack).groups()[0]
        )
        num_edicao = remove_tags(num_edicao)
        date = dateparser.parse(remove_tags(date), languages=["pt"]).date()

        return event_target, num_edicao, date

    def _format_filename(self, num_edicao: str, date):
        filename = f"{self.allowed_domains[0].replace('.','')}-{num_edicao}-{date}.pdf"
        file_path = Path(f"{FILES_STORE}full/{filename}")
        return file_path

    def parse(self, response):
        records = response.css(".DataGrid").xpath(
            ".//*[contains(@class, 'DataGridItems')] | .//*[contains(@class, 'DataGridAlternating')]"
        )
        VIEW_STATE, EVENT_VALIDATION = self._get_form_params(response)
        for element in records:
            EVENT_TARGET, num_edicao, date = self._parse_table_elements(element)
            file_path = self._format_filename(num_edicao, date)
            item = Gazette(
                date=date,
                is_extra_edition=False,
                territory_id=self.TERRITORY_ID,
                power="executive_legislature",
                scraped_at=datetime.utcnow(),
                files=[{"path": file_path}],
            )
            yield FormRequest.from_response(
                response,
                callback=self._save_pdf,
                cb_kwargs=dict(path=file_path, item=item),
                formname="aspnetForm",
                formdata={
                    "__EVENTTARGET": EVENT_TARGET,
                    # "__EVENTTARGET": "ctl00$ContentPlaceHolder1$dtgResultado$ctl03$ctl00",
                    "__EVENTARGUMENT": "",
                    "__VIEWSTATE": VIEW_STATE,
                    "__EVENTVALIDATION": EVENT_VALIDATION,
                    "ctl00$ContentPlaceHolder1$dt_inicio": "01/01/2010",
                    # "ctl00$ContentPlaceHolder1$dt_final": self.TODAY,
                    "ctl00$ContentPlaceHolder1$dt_final": "31/01/2010",
                },
                method="POST",
                dont_click=True,
                dont_filter=True,
            )
        for element in (
            response.css(".DataGrid")
            .xpath(".//*[contains(@class, 'DataGridPager')]")
            .getall()
        ):
            event_target = unquote(
                re.search(self.JAVASCRIPT_POSTBACK_REGEX, element).groups()[0]
            )
            # VIEW_STATE, EVENT_VALIDATION = self._get_form_params(response)
            yield FormRequest.from_response(
                response,
                callback=self.parse,
                formname="aspnetForm",
                formdata={
                    "__EVENTTARGET": event_target,
                    "__EVENTARGUMENT": "",
                    "__VIEWSTATE": VIEW_STATE,
                    "__EVENTVALIDATION": EVENT_VALIDATION,
                    "ctl00$ContentPlaceHolder1$dt_inicio": "01/01/2010",
                    # "ctl00$ContentPlaceHolder1$dt_final": self.TODAY,
                    "ctl00$ContentPlaceHolder1$dt_final": "31/01/2010",
                },
                clickdata={
                    "name": "ctl00$ContentPlaceHolder1$PsaToolBar1$btnSelecionar"
                },
                method="POST",
                dont_click=True,
                dont_filter=True,
            )

