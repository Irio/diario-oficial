from datetime import datetime
from urllib.parse import parse_qsl

import scrapy
from dateparser import parse
from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider
from parsel import Selector


class SeAracajuSpider(BaseGazetteSpider):
    TERRITORY_ID = "2800308"
    name = "se_aracaju"

    custom_settings = {"CONCURRENT_REQUESTS": 12}

    start_urls = [
        "http://sga.aracaju.se.gov.br:5011/legislacao/faces/diario_form_pesq.jsp"
    ]

    def start_requests(self, cookiejar=None):
        for url in self.start_urls:
            meta = {"cookiejar": cookiejar} if cookiejar else {}
            yield scrapy.Request(url, meta=meta, dont_filter=True)

    def parse(self, response):
        mesano_param = response.css("[value=mesano]::attr(name)").get()
        yield scrapy.FormRequest.from_response(
            response,
            formdata={mesano_param: "mesano"},
            callback=self.parse_search_by_month_and_year,
            dont_filter=True,
            meta={"cookiejar": response.meta.get("cookiejar")},
        )

    def _make_year_month_request(self, response, formdata=None):
        container_id = response.css("select::attr(onchange)").re_first(
            r"containerId\':\'(.+)\'"
        )
        mes_param = response.xpath(
            "//td[contains(./span//text(), 'Mês')]/following-sibling::td//select/@name"
        ).get()
        ano_param = response.xpath(
            "//td[contains(./span//text(), 'Ano')]/following-sibling::td//select/@name"
        ).get()
        search_button_param = response.css(".botaoCadastrarPesq::attr(id)").get()

        year, month = cookiejar = response.meta.get("cookiejar")
        if not formdata:
            # request the first page for the pair (year, month)
            return scrapy.FormRequest.from_response(
                response,
                formdata={
                    "AJAXREQUEST": container_id,
                    ano_param: str(year),
                    mes_param: str(month),
                    search_button_param: search_button_param,
                },
                meta={"cookiejar": cookiejar},
                callback=self.parse_page_result,
            )
        else:
            # request the next page from the pagination widget
            return scrapy.FormRequest(
                response.url,
                formdata=formdata,
                meta={"cookiejar": cookiejar},
                callback=self.parse_page_result,
            )

    def parse_search_by_month_and_year(self, response):
        if not response.meta.get("cookiejar", False):
            all_years_available = response.xpath(
                "//td[contains(./span//text(), 'Ano')]/following-sibling::td//option/@value"
            ).getall()
            for year in all_years_available:
                for month in range(1, 13):
                    yield from self.start_requests(cookiejar=(year, month,))
        else:
            yield self._make_year_month_request(response)

    def parse_page_result(self, response):
        page = Selector(response.text)
        page.remove_namespaces()

        for gazette in page.css(".rich-table-cell"):
            gazette.remove_namespaces()
            gazette_number = gazette.xpath(".//table//td/text()").get()
            if gazette_number is None:
                continue

            gazette_date = gazette.css(".rich-panel-header::text").get()
            file_url = f"http://sga.aracaju.se.gov.br:5011/diarios/{gazette_number}.pdf"
            yield Gazette(
                date=parse(gazette_date, languages=["pt"]).date(),
                is_extra_edition=False,
                file_urls=[file_url],
                power="executive",
            )

        next_page_param = page.css(".rich-datascr::attr(id)").get()
        next_page = page.css(".rich-datascr-act + .rich-datascr-inact::text").get()
        if next_page_param and next_page:
            last_formdata = dict(parse_qsl(response.request.body.decode()))
            formdata = {
                **last_formdata,
                next_page_param: next_page,
                "AJAX:EVENTS_COUNT": "1",
            }
            yield self._make_year_month_request(response, formdata)


# TODO
# - Verificar o link de diários antigos - que parecem que não seguem o padrão {numero}.pdf
