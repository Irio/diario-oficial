import dateparser
import datetime as dt

from dateutil.relativedelta import relativedelta

import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class SpGuaruja(BaseGazetteSpider):

    TERRITORY_ID = "3518701"
    name = "sp_guaruja"
    allowed_domains = ["guaruja.sp.gov.br"]
    start_urls = ["http://www.guaruja.sp.gov.br/edicoes-diario-oficial/"]

    def __init__(self, start_date=None, end_date=None, *args, **kwargs):
        self.start_date = dt.date(2009, 1, 1)
        self.end_date = dt.date.today()

        super(SpGuaruja, self).__init__(start_date, end_date, *args, **kwargs)

        self.logger.debug(
            "Start date is {date}".format(date=self.start_date.isoformat())
        )
        self.logger.debug("End date is {date}".format(date=self.end_date.isoformat()))

    def parse(self, response):
        calendar_id = response.xpath(
            '//div[@class="mec-search-form mec-totalcal-box"]/div/@class'
        ).get()

        # This ID is prefixed by 'mec_search_form_'. IE: mec_search_form_18101
        calendar_id = calendar_id.replace("mec_search_form_", "")

        target_date = self.start_date
        data = {
            "action": "mec_full_calendar_switch_skin",
            "skin": "monthly",
            "atts[skin]": "full_calendar",
            "atts[show_past_events]": "1",
            "atts[id]": calendar_id,
            "apply_sf_date": "1",
        }

        while target_date <= self.end_date:
            data.update(
                {
                    "sf[month]": f"{target_date.month:02}",
                    "sf[year]": str(target_date.year),
                }
            )
            yield scrapy.FormRequest(
                url="https://www.guaruja.sp.gov.br/wp-admin/admin-ajax.php",
                formdata=data,
                method="POST",
                callback=self.parse_events,
            )
            target_date = target_date + relativedelta(months=1)

    def parse_events(self, response):
        clean_response = self.clean_response_body(response)
        for event_link in clean_response.xpath('//h4[@class="mec-event-title"]'):
            file_url = event_link.xpath("a/@href").get()
            event_date = event_link.xpath(
                'ancestor::div[@class="mec-calendar-events-sec"]/@data-mec-cell'
            ).get()
            event_date = dt.datetime.strptime(event_date, "%Y%m%d").date()
            if event_date > self.end_date:
                # We could break here, but god only
                # knows if they sort the output.
                continue

            yield Gazette(
                date=event_date,
                file_urls=[file_url],
                is_extra_edition=False,
                territory_id=self.TERRITORY_ID,
                power="executive_legislature",
                scraped_at=dt.datetime.utcnow(),
            )

    @classmethod
    def clean_response_body(cls, response):
        # Response body here is a messed up double back-slashed string
        body = response.body[1:-1]
        body = (
            body.decode("utf-8")
            .replace('\\"', '"')
            .replace("\\r", "")
            .replace("\\n", "\n")
            .replace("\/", "/")
            .encode("utf-8")
        )
        return response.replace(body=body)
