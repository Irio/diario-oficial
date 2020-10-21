from datetime import datetime

import dateparser
from scrapy import Request

from gazette.spiders.base import BaseGazetteSpider
from gazette.items import Gazette


class PaAnanindeuaSpider(BaseGazetteSpider):

    TERRITORY_ID = "1500800"
    name = "pa_ananindeua"
    allowed_domains = ["ananindeua.pa.gov.br"]
    start_urls = ["http://www.ananindeua.pa.gov.br/diario/inicio/diarios-pdf"]
    FILE_ELEMENT_CSS = "div#content div div#online_arquivo a::attr(href)"
    DATE_ELEMENT_CSS = "div#content div div#online_data::text"
    DATE_FORMAT = "%d/%m/%Y"

    def parse(self, response):
        # Year ids are not truly sequential, this offset prevent from missing someone
        offset = 5
        avaliable_years_ids = datetime.now().year - 2008

        for year_id, month_id in zip(
            range(1, avaliable_years_ids + offset), range(1, 13)
        ):
            yield Request(
                url=f"{response.url}?id={year_id}&mes={month_id}",
                callback=self.parse_month,
            )

    def parse_month(self, response):
        file_urls = response.css(self.FILE_ELEMENT_CSS).extract()
        dates = response.css(self.DATE_ELEMENT_CSS).extract()

        for date_str, file_url in zip(dates, file_urls):
            date = dateparser.parse(date_str, date_formats=[self.DATE_FORMAT]).date()
            url = response.urljoin(file_url)

            yield Gazette(
                date=date,
                file_urls=[url],
                is_extra_edition="extra" in url.lower(),
                territory_id=self.TERRITORY_ID,
                scraped_at=datetime.utcnow(),
                power="executive",
            )
