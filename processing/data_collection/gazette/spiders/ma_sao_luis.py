# -*- coding: utf-8 -*-
import dateparser
from datetime import datetime
from scrapy_splash import SplashRequest

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider
from scrapy.shell import inspect_response


class MaSaoLuisSpider(BaseGazetteSpider):
    MUNICIPALITY_ID = '2111300'
    name = 'ma_sao_luis'
    allowed_domains = ['www.semad.saoluis.ma.gov.br']
    start_urls = ['http://www.semad.saoluis.ma.gov.br:8090/easysearch/']

    def start_requests(self):
        lua_script = """
function main(splash, args)
    splash:init_cookies(splash.args.cookies)
    splash:go(args.url)
    getElementByXPath = splash:jsfunc([[
        function (path) {
            return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        }
    ]])
    splash:wait(12)
    tamanho_pagina = getElementByXPath("//tbody/tr/td/div[@class='GPFMNGWKN' and text()='20']")
    tamanho_pagina:mouse_click()
    splash:wait(3)
    tamanho_1 = getElementByXPath("//div[1]/div/span[@class='GPFMNGWKGC']")
    tamanho_1:mouse_click()
    splash:wait(4)
    return {html = splash:html(), cookies = splash:get_cookies()}
end
"""
        for url in self.start_urls:
            yield SplashRequest(
                url=url, callback=self.parse, endpoint='execute',
                args={'lua_source': lua_script, 'timeout': 90})

    def parse(self, response):
        """
        @url
        @returns items 1
        @scrapes date file_urls is_extra_edition
                 municipality_id power scraped_at
        """
        # dates with gazettes available inside the following hidden textarea:
        date = response.xpath(("//body/div/div/div/div/div/div/div/div/div"
                               "/div/div/div/div/div/"
                               "table/tbody/tr[1]/td[2]/div/text()"))
        date = date.extract_first()
        date = dateparser.parse(date)
        if date.year < 2015:
            print('ano de 2015, parando. data: {}'.format(date))
            raise StopIteration

        url = response.xpath(("//tbody/tr[4]/td[1]/a"
                              "[@class='campoResultadoDownload']"
                              "/@href")).extract_first()
        url = response.url[:39] + url
        yield Gazette(
            date=date,
            file_urls=[url],
            is_extra_edition=False,
            municipality_id=self.MUNICIPALITY_ID,
            scraped_at=datetime.utcnow(),
            power='executive'
        )
        lua_script = """
function main(splash, args)
    splash:init_cookies(splash.args.cookies)
    splash:go(args.url)
    getElementByXPath = splash:jsfunc([[
        function (path) {
            return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        }
    ]])
    splash:wait(18)
    tamanho_pagina = getElementByXPath("//tbody/tr/td/div[@class='GPFMNGWKN' and text()='20']")
    tamanho_pagina:mouse_click()
    splash:wait(3)
    tamanho_1 = getElementByXPath("//div[1]/div/span[@class='GPFMNGWKGC']")
    tamanho_1:mouse_click()
    splash:wait(6)
    page_box = getElementByXPath("//div[@class='GPFMNGWNP']/input[@class='gwt-TextBox GPFMNGWOJ GPFMNGWIK']")
    page_box:send_keys("<Delete>")
    page_box:send_text(args.page_number)
    page_box:send_keys("<Return>")
    splash:wait(6)
    return {html = splash.html(), cookies = splash:get_cookies()}
end
"""
        for page_number in range(2, 7000):
            yield SplashRequest(
                url=response.url, callback=self.parse, endpoint='execute',
                args={'lua_source': lua_script, 'timeout': 90,
                      'page_number': str(page_number)})
