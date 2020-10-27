from dateparser import parse
import datetime as dt

import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class RsBentoGoncalvesSpider(BaseGazetteSpider):
    TERRITORY_ID = "4302105"
    name = "rs_bento_goncalves"
    allowed_domains = ["bentogoncalves.rs.gov.br"]
    start_urls = ["http://www.bentogoncalves.rs.gov.br/diario-oficial"]
    start_date = dt.date(2014, 9, 19)

    def parse(self, response):
        for gazette in self.parse_gazettes(response):
            yield gazette

        pagesURLSelector = '//*[@id="conteudo"]/div[2]/ul/div[2]/div/a/@href'
        pages = response.xpath(pagesURLSelector).getall()

        for page in pages:
            url = "http://www." + self.allowed_domains[0] + "/" + page
            yield scrapy.Request(url, self.parse_gazettes)

    def parse_gazettes(self, response):
        gazetteLinksSelector = '//*[@id="conteudo"]/div[2]/ul/li/p/a/@href'
        gazetteTitleSelector = '//*[@id="conteudo"]/div[2]/ul/li/p/a/strong/text()'

        gazetteLinks = list(
            map(self.linkToGazette, response.xpath(gazetteLinksSelector).getall())
        )
        gazetteTitles = response.xpath(gazetteTitleSelector).getall()
        gazetteDates = list(map(self.gazetteDate, gazetteTitles))
        gazetteIsExtraEdition = list(map(self.isExtraEdition, gazetteTitles))

        for date, link, isExtraEdition in zip(
            gazetteDates, gazetteLinks, gazetteIsExtraEdition
        ):
            if link and date:
                yield Gazette(
                    date=date,
                    file_urls=[link],
                    is_extra_edition=isExtraEdition,
                    territory_id=self.TERRITORY_ID,
                    power="executive",
                    scraped_at=dt.datetime.utcnow(),
                )

    def linkToGazette(self, elem):
        if ".pdf" in elem:
            return "http://www." + self.allowed_domains[0] + "/" + elem

    def gazetteDate(self, elem):
        splitedElem = elem.split("/")
        try:
            return dt.date(
                int(splitedElem[2][:4]),
                int(splitedElem[1][:2]),
                int(splitedElem[0][-2:]),
            )
        except:
            print("No date found.")
            return None

    def isExtraEdition(self, elem):
        extraStrings = ["extra", "suplementar", "complementar"]
        elemLower = elem.lower()
        for extraString in extraStrings:
            if extraString in elemLower:
                return True
        return False
