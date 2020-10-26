import datetime as dt

from scrapy.http import FormRequest

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class PrFozDoIguacuSpider(BaseGazetteSpider):
    TERRITORY_ID = "4108304"
    BASE_URL = "http://www.pmfi.pr.gov.br"
    name = "pr_foz_do_iguacu"
    allowed_domains = ["pmfi.pr.gov.br"]
    start_urls = [f"{BASE_URL}/utilidades/diario/index.xhtml"]

    def parse(self, response):
        selector = '(//span[@class="ui-paginator-current"])[1]/text()'
        paginator_text = response.xpath(selector)
        quantity_of_documents = int(paginator_text.re_first("\([\d]+ de ([\d]+)\)")) + 1

        data = {
            "formDiarioOficialView": "formDiarioOficialView",
            "formDiarioOficialView:dtdiario": "formDiarioOficialView:dtdiario",
            "formDiarioOficialView:dtdiario_encodeFeature": "true",
            "formDiarioOficialView:dtdiario_first": "0",
            "formDiarioOficialView:dtdiario_pagination": "false",
            "formDiarioOficialView:dtdiario_rows": str(quantity_of_documents),
        }
        return FormRequest(response.url, formdata=data, callback=self.parse_items)

    def parse_items(self, response):
        lines = response.xpath('//tr[@role="row"]')
        for line in lines:
            date, url, is_extra_edition = self.get_gazette_data(line)

            yield Gazette(
                date=date,
                file_urls=[f"{self.BASE_URL}{url}"],
                is_extra_edition=is_extra_edition,
                power="executive_legislature",
            )

    @staticmethod
    def get_gazette_data(line):
        _, content_column, *_, date_column, download_column = line.xpath("td")

        content = content_column.xpath("text()").extract_first()

        is_extra_edition = "EDIÇÃO EXTRAORDINÁRIA" in content
        date = dt.datetime.strptime(
            date_column.xpath("text()").extract_first(), "%d/%m/%Y"
        ).date()
        url = download_column.css("a::attr(href)").extract_first()

        return date, url, is_extra_edition
