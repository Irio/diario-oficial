# -*- coding: utf-8 -*-
import dateparser
from datetime import datetime
from scrapy_splash import SplashRequest

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider
from scrapy.shell import inspect_response


class MaSaoLuisSpider(BaseGazetteSpider):
    TERRITORY_ID = '2111300'
    name = 'ma_sao_luis'
    allowed_domains = ['www.semad.saoluis.ma.gov.br']
    start_url = 'http://www.semad.saoluis.ma.gov.br:8090/easysearch/'

    lua_script = """
function wait_for_element(splash, css, value, maxwait)
  -- Wait until a selector matches an element
  -- and it contains a specific value
  -- in the page. Return an error if waited more
  -- than maxwait seconds.
  if maxwait == nil then
      maxwait = 10
  end
  return splash:wait_for_resume(string.format([[
    function main(splash) {
      var selector = '%s';
      var value = %s;
      var maxwait = %s;
      var end = Date.now() + maxwait*1000;
      function check() {
        if(document.querySelector(selector) && document.querySelector(selector).value === value) {
          splash.resume('Element found');
        } else if(Date.now() >= end) {
          var err = 'Timeout waiting for element';
          splash.error(err + " " + selector);
        } else {
          setTimeout(check, 200);
        }
      }
      check();
    }
  ]], css, value, maxwait))
end

function main(splash, args)
    getElementByXPath = splash:jsfunc([[
    function (path) {
        return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    }
    ]])
    splash:go(args.url)
    wait_for_element(splash, 'a.campoResultadoDownload', '1', 40)
    page_input_box = getElementByXPath("//div[@class='GPFMNGWNP']/input[@class='gwt-TextBox GPFMNGWOJ GPFMNGWIK']")
    page_input_box:send_keys("<Delete>")
    page_input_box:send_text(args.page_number)
    page_input_box:send_keys("<Return>")
    wait_for_element(splash, 'a.campoResultadoDownload', args.page_number, 40)
    return {html = splash.html(), cookies = splash:get_cookies(), png = splash.png()}
end
"""

    def start_requests(self):
        """
        @url
        @returns items 1
        @scrapes date file_urls is_extra_edition
                 municipality_id power scraped_at
        """
        self.logger.info("sent page %d to splash", 1)
        yield SplashRequest(
            url=self.start_url, callback=self.parse,
            endpoint='execute', args={'lua_source': self.lua_script,
                                      'page_number': '1', 'timeout': 90})

    def parse(self, response):
        for gazette_table in response.xpath(
                "//table[contains(@class, 'tabelaResultado')]"):
            date = gazette_table.xpath(
                    ".//tbody/tr[1]/td[2]/div/text()").extract_first()
            self.logger.info("ma_sao_luis_spider: got gazette for day %s",
                             date)
            date = dateparser.parse(date, settings={'DATE_ORDER': 'DMY'})

            url = gazette_table.xpath((".//tbody/tr/td/a"
                                       "[contains(text(), 'Download')]"
                                       "/@href")).extract_first()
            url = response.urljoin(url)
            extra_edition = (gazette_table.xpath(
                ".//div[contains(text(), 'Suplemento')]").extract_first()
                is not None)
            yield Gazette(
                date=date, file_urls=[url],
                is_extra_edition=extra_edition,
                territory_id=self.TERRITORY_ID,
                scraped_at=datetime.utcnow(), power='executive')
        page_number = int(response._splash_args()['page_number']) + 1
        self.logger.info("sent page %d to splash", page_number)
        yield SplashRequest(
            url=response.url, callback=self.parse, endpoint='execute',
            args={'lua_source': self.lua_script,
                  'page_number': str(page_number), 'timeout': '90'})
