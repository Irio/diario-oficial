from dateparser import parse
import datetime as dt
import re

import scrapy

from gazette.items import Gazette

class MgMontesClarosSpider(scrapy.Spider):
    MUNICIPALITY_ID = '3143302'
    name = 'mg_montes_claros'
    
    allowed_domains = ['montesclaros.mg.gov.br']
    start_urls = ['http://www.montesclaros.mg.gov.br/diariooficial/']

    initialized=False
    available_pages = []

    def initalize(self, response):
        self.initialized=True
        pages = response.css('#menu-principal ul li a::attr(href)').extract()
        self.available_pages = iter(pages)

    def parse(self, response):
        """
        @url http://www.montesclaros.mg.gov.br/diariooficial/
        @returns requests 1 1
        @scrapes date file_urls is_extra_edition municipality_id power scraped_at
        """
        if not self.initialized:
            self.initalize(response)

        for gazette_node in response.css('.entry-content li a'):
           
            title = gazette_node.xpath('text()').extract_first()
            if not title:
                title = gazette_node.xpath('span/text()').extract_first()

            date = self.get_date(title)
            
            if not date:
                self.logger.info('The title "%s" don´t like a valid Gazzete Item', title)
                continue

            yield Gazette(
                date=date,
                file_urls=[ gazette_node.xpath('@href').extract_first() ],
                is_extra_edition=True if 'EDIÇÃO EXTRA' in title.upper() else False,
                municipality_id=self.MUNICIPALITY_ID,
                power='executive_legislature',
                scraped_at=dt.datetime.utcnow(),
            )
        
        try:
            next_page_url = next(self.available_pages)
            yield response.follow(next_page_url)
        except:
           return
        
    @staticmethod
    def get_date(title):
        d = re.search("([0-9]{2}\-[0-9]{2}\-[0-9]{2})", title)
        if not d:
            return
        d = d[0].split('-')
        return dt.date(2000+int(d[2]), int(d[1]), int(d[0]))

     