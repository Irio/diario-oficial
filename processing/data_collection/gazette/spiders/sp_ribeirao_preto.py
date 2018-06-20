from gazette.items import Gazette
import scrapy
from gazette.spiders.base import BaseGazetteSpider
from datetime import date, timedelta, datetime


class SpRibeiraoPretoSpider(BaseGazetteSpider):
    """Ribeirao Preto's website uses Java Server Faces
    as their framework. This fact makes the scraper behave
    a little bit differently than the other ones.
    """

    MUNICIPALITY_ID = '3543402'
    SEARCH_PAGE_URL = 'https://www.ribeiraopreto.sp.gov.br/J015/pesquisaData.xhtml'
    name = 'sp_ribeirao_preto'

    """Without this delay the scraped
    website seems to block connections
    after the first requests.
    """
    download_delay = 0.25

    """This spider needs a start date because
    we don't have a page with all the gazettes, we
    are required to input a date in the first request
    in order to obtain a gazette. Because of this we
    define a default start date to be used if
    BaseGazetteSpider does not provide us with a value.
    """
    DEFAULT_START_DATE = date(2015, 1, 1)

    def start_requests(self):
        """We need three requests to download a single day gazette.
        It seems that there is no page with links to the gazettes,
        so the first step is to generate the dates (that's why we don't
        have a start_urls field, but a start_requests method). Each
        gazette_date is then mapped to a scrapy.Request instance, using
        a unique cookiejar id. This is important because the session state
        is heavily used by the application, so each gazette_date needs its
        own session cookies.
        """
        start_date = self.start_date if hasattr(self, 'start_date') else self.DEFAULT_START_DATE
        end_date = date.today()
        current_date = start_date
        cookiejar_id = 1
        while current_date <= end_date:
            yield scrapy.Request(self.SEARCH_PAGE_URL,
                                 dont_filter=True,
                                 meta={'gazette_date': current_date,
                                       'cookiejar': cookiejar_id})
            current_date += timedelta(days=1)
            cookiejar_id = cookiejar_id + 1

    def parse(self, response):
        """The first request is here just to give us
        a fresh session with the server.

        The only information we need to scrap here is the
        javax.faces.ViewState value which resides inside an
        input hidden.
        """
        view_state_xpath = '//*[@id="j_id1:javax.faces.ViewState:0"]/@value'
        view_state_id = response.xpath(view_state_xpath).extract_first()
        gazette_date = response.meta['gazette_date']
        formatted_gazette_date = gazette_date.strftime('%d/%m/%Y')
        return scrapy.FormRequest(self.SEARCH_PAGE_URL,
                                  dont_filter=True,
                                  formdata={'javax.faces.partial.ajax': 'true',
                                            'javax.faces.source': 'formdiario:j_idt91',
                                            'javax.faces.partial.execute': 'formdiario:j_idt91',
                                            'javax.faces.partial.render': '@all',
                                            'javax.faces.behavior.event': 'dateSelect',
                                            'javax.faces.partial.event': 'dateSelect',
                                            'formdiario': 'formdiario',
                                            'formdiario:j_idt91_input': formatted_gazette_date,
                                            'javax.faces.ViewState': view_state_id},
                                  meta={'gazette_date': gazette_date,
                                        'cookiejar': response.meta['cookiejar']},
                                  callback=self.parse_search_results)

    def parse_search_results(self, response):
        """The second request is AJAX based, meaning we can't use
        xpath in the response directly. First we need to extract the
        HTML content from one of the //partial-response/changes/update tags,
        the one with a specific id. We then parse this text as HTML and check if
        the download button is there (there may be many in a single day).
        If any download button is found then a list of file_requests
        is populated and a Gazette instance is returned. See
        gazette.pipelines.CustomFilesPipeline for more information
        on the file_requests field.
        """

        page_update_xpath = '//update[@id="javax.faces.ViewRoot"]/text()'
        page_update = response.xpath(page_update_xpath).extract_first()
        page_update_selector = scrapy.Selector(text=page_update)

        view_state_update_xpath = '//update[@id="j_id1:javax.faces.ViewState:0"]/text()'
        view_state_id = response.xpath(view_state_update_xpath).extract_first()

        file_requests = self.collect_file_requests(page_update_selector,
                                                   view_state_id,
                                                   response.meta['cookiejar'])

        if file_requests:
            return Gazette(date=response.meta['gazette_date'],
                           is_extra_edition=False,
                           municipality_id=self.MUNICIPALITY_ID,
                           power='executive_legislature',
                           scraped_at=datetime.utcnow(),
                           file_requests=file_requests)

    def collect_file_requests(self, page_update_selector, view_state_id, cookiejar):
        file_requests = []

        def check_download_button(button_id_suffix):
            download_btn_xpath = f'//button[@id="formdiario:j_idt{button_id_suffix}"]'
            download_btn = page_update_selector.xpath(download_btn_xpath).extract_first()
            if download_btn:
                file_requests.append({'url': self.SEARCH_PAGE_URL,
                                      'formdata': {'javax.faces.ViewState': view_state_id,
                                                   'formdiario': 'formdiario',
                                                   f'formdiario:j_idt{button_id_suffix}': ''},
                                      'cookiejar': cookiejar})
            return download_btn is not None

        if check_download_button(100): # there is a single gazette for this day
            pass
        else:
            if check_download_button(101): # there are multiple gazettes for this day
                button_id_suffix = 103 # the 102 button is NOT a download link
                while check_download_button(button_id_suffix): # there may be more than two gazettes
                    button_id_suffix = button_id_suffix + 1

        return file_requests
