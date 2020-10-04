import datetime
import logging

from scrapy import Request, signals


class GazetteDateFilteringSpiderMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        s.logger = logging.getLogger(f"{__name__}.{cls.__name__}")
        return s

    def process_spider_output(self, response, result, spider):
        for request_or_item in result:
            if isinstance(request_or_item, Request):
                if request_or_item.dont_filter is True:
                    yield request_or_item
                    continue

                gazette_date = request_or_item.meta.get("gazette_date")
                if gazette_date is None:
                    yield request_or_item
                    continue
            else:
                gazette_date = request_or_item["date"]

            if not (
                self.filtered_by_start_date(gazette_date, spider)
                or self.filtered_by_end_date(gazette_date, spider)
            ):
                yield request_or_item
            else:
                self.logger.warning(
                    f"Request or item outside of the desired date range was dropped: {request_or_item}"
                )

    def process_start_requests(self, start_requests, spider):
        yield from self.process_spider_output(None, start_requests, spider)

    def filtered_by_start_date(self, date, spider):
        if not hasattr(spider, "start_date"):
            return False

        return spider.start_date > self.parse_date(date, spider.start_date)

    def filtered_by_end_date(self, date, spider):
        if not hasattr(spider, "end_date"):
            return False

        return spider.end_date < self.parse_date(date, spider.end_date)

    def parse_date(self, date, default_date):
        if isinstance(date, dict):
            year = date.get("year")
            month = date.get("month", default_date.month)
            day = date.get("day", default_date.day)
            parsed_date = datetime.date(year, month, day)
        elif isinstance(date, datetime.date):
            parsed_date = date
        elif isinstance(date, datetime.datetime):
            parsed_date = date.date()
        else:
            raise Exception(f"Date {date} cannot be parsed.")

        return parsed_date


class GazetteSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.
        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.
        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.
        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.
        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class GazetteDownloaderMiddleware:

    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.
        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.
        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.
        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
