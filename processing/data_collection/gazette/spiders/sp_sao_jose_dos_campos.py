import dateparser

from scrapy import FormRequest
from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class SpSaoJoseDosCamposSpider(BaseGazetteSpider):
    TERRITORY_ID = "3549904"

    GAZETTE_NAME_CSS = "td:last-child a::text"
    GAZETTE_URL_CSS = "td:last-child a::attr(href)"
    GAZETTE_DATE_CSS = "td:nth-child(2)::text"
    NEXT_PAGE_LINK_CSS = ".paginador_anterior_proxima a"
    JAVASCRIPT_POSTBACK_REGEX = r"javascript:__doPostBack\('(.*)',''\)"

    allowed_domains = ["servicos2.sjc.sp.gov.br"]
    name = "sp_sao_jose_dos_campos"
    start_urls = [
        "http://servicos2.sjc.sp.gov.br/servicos/portal_da_transparencia/boletim_municipio.aspx"
    ]

    def parse(self, response):
        for element in response.css("#corpo table tr"):
            if element.css("th").extract():
                continue

            date = element.css(self.GAZETTE_DATE_CSS).extract_first()
            date = dateparser.parse(date, languages=["pt"]).date()
            url = element.css(self.GAZETTE_URL_CSS).extract_first()
            gazette_title = element.css(self.GAZETTE_NAME_CSS).extract_first()
            is_extra = "Extra" in gazette_title

            yield Gazette(
                date=date,
                file_urls=[url],
                is_extra_edition=is_extra,
                power="executive_legislature",
            )

        for element in response.css(self.NEXT_PAGE_LINK_CSS):
            if not element.css("a::text").extract_first() == "Próxima":
                continue

            event_target = element.css("a::attr(href)")
            event_target = event_target.re(self.JAVASCRIPT_POSTBACK_REGEX).pop()

            yield FormRequest.from_response(
                response,
                callback=self.parse,
                formname="aspnetForm",
                formxpath="//form[@id='aspnetForm']",
                formdata={"__EVENTARGUMENT": "", "__EVENTTARGET": event_target},
                dont_click=True,
                dont_filter=True,
                method="POST",
            )
