# -*- coding: utf-8 -*-
from dateparser import parse

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class PrCascavelSpider(BaseGazetteSpider):
    TERRITORY_ID = "4104808"
    name = "pr_cascavel"
    allowed_domains = ["cascavel.pr.gov.br"]
    start_urls = ["http://www.cascavel.pr.gov.br/servicos/orgao_oficial.php"]
    download_url = "http://www.cascavel.pr.gov.br/anexos/{}"

    def parse(self, response):
        for row in response.xpath("//table//tr[position()>1]"):
            date = row.xpath(".//td[2]//font//text()").extract_first()
            date = parse(date, languages=["pt"]).date()
            for link in row.xpath(".//td[3]//a"):
                link_text = link.xpath(".//text()").extract_first()
                power = "executive" if "Executivo" in link_text else "legislature"
                url = response.urljoin(link.xpath("./@href").extract_first(""))
                yield Gazette(
                    date=date, file_urls=[url], is_extra_edition=False, power=power,
                )
        next_page_xpath = '//a[@title="Próxima página"]/@href'
        next_page_url = response.xpath(next_page_xpath).extract_first()
        if next_page_url:
            yield response.follow(next_page_url)
