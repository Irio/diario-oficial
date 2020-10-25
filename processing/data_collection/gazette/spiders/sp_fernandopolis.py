from datetime import datetime

from dateparser import parse
import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class SpFernandopolis(BaseGazetteSpider):
    TERRITORY_ID = "3515509"
    name = "sp_fernandopolis"
    start_urls = [
        "https://diariotransparente.com.br/publicacoes/frame/spfernandopolispm"
    ]

    def parse(self, response):
        list_pubs = response.css("div.row")
        for pub in list_pubs:
            link_date = pub.css("h3>a")
            date = link_date.css("::text").get()
            date = parse(date, languages=["pt"]).date()
            link = response.urljoin(link_date.attrib["href"])
            is_extra_edition = bool(pub.xpath(".//li[contains(., 'EXTRA')]"))
            yield Gazette(
                date=date,
                file_urls=[link],
                is_extra_edition=is_extra_edition,
                municipality_id=self.TERRITORY_ID,
                power="executive",
                scraped_at=datetime.utcnow(),
            )
