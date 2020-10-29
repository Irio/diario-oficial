from datetime import date, datetime
import re

from dateparser import parse
import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class SpVinhedoSpider(BaseGazetteSpider):
    allowed_domains = ["vinhedo.sp.gov.br"]
    start_urls = ["http://vinhedo.sp.gov.br/arquivos/?wpdmc=boletim-municipal"]
    name = "sp_vinhedo"
    start_date = date(2010, 12, 9)
    TERRITORY_ID = "3556701"

    def parse(self, response):
        page = response.xpath('//*[@class="next page-numbers"]//@href')
        last_page = re.search(r"(paged=)(\d{,2})", page.get()).group(2)
        for i in range(1, int(last_page)):
            response.urljoin(page.get())
            gazettes = response.css('table tbody tr')
            for gazette in gazettes:
                data = gazette.css('td')
                edition = data.css('.package-title::text').get()
                date = data.css('.hidden-sm::text').get()
                link = data.css('[onclick]').get()
                yield Gazette(
                    date=parse(date, languages=["pt"]).date(),
                    edition_number=re.search(
                        r"(ção|xtra|úmero)(\D*)(\d{1,4})", edition
                    ).group(3),
                    file_urls=[re.search(r"(htt(.)+)(\';)", link).group(1)],
                    is_extra_edition=bool(re.search(r"[Ee]xtra", edition)),
                    power="executive_legislative",
                    scraped_at=datetime.utcnow(),
                    territory_id=self.TERRITORY_ID,
                )
