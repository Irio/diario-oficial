from datetime import datetime

import scrapy
from scrapy.exceptions import NotConfigured


class BaseGazetteSpider(scrapy.Spider):
    def __init__(self, start_date=None, end_date=None, *args, **kwargs):
        super(BaseGazetteSpider, self).__init__(*args, **kwargs)

        if not hasattr(self, "TERRITORY_ID"):
            raise NotConfigured("Please set a value for `TERRITORY_ID`")

        if start_date is not None:
            try:
                self.start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
                self.logger.info(f"Collecting gazettes from {self.start_date}")
            except ValueError:
                self.logger.exception(
                    f"Unable to parse {start_date}. Use %Y-%m-d date format."
                )
                raise
        else:
            self.logger.info("Collecting all gazettes available from the beginning")

        if end_date is not None:
            try:
                self.end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
                self.logger.info(f"Collecting gazettes until {self.end_date}")
            except ValueError:
                self.logger.exception(
                    f"Unable to parse {end_date}. Use %Y-%m-d date format."
                )
                raise
        else:
            self.logger.info("Collecting all gazettes available until today")
