from dateutil.parser import parse

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class PbCampinaGrandeSpiderExecutive(BaseGazetteSpider):
    TERRITORY_ID = "2504009"
    allowed_domains = ["campinagrande.pb.gov.br"]
    name = "pb_campina_grande"
    start_urls = ["https://campinagrande.pb.gov.br/semanario-oficial/"]

    def parse(self, response):
        years_urls = response.css(".secretaria-text a::attr(href)").getall()
        yield from response.follow_all(years_urls, self.parse_year)

    def parse_year(self, response):
        months_urls = response.css(".secretaria-text a::attr(href)").getall()
        yield from response.follow_all(months_urls, self.parse_month)

    def parse_month(self, response):
        editions = response.css(".td_module_1")
        if not editions:
            self.logger.debug(f"No editions found at {response.url}")
        else:
            for edition in editions:
                url = edition.css("a::attr(href)").get()
                date = parse(edition.css("time::attr(datetime)").get()).date()
                yield response.follow(url, self.parse_issue, meta={"date": date})

    def parse_issue(self, response):
        urls = response.css(".td-post-content a::attr(href)").getall()
        title = response.css("h1::text").get().lower()

        yield Gazette(
            date=response.meta.get("date"),
            file_urls=urls,
            is_extra_edition="separata" in title,
            power="executive",
        )
