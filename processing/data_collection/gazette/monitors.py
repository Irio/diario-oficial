from spidermon import Monitor, MonitorSuite, monitors


@monitors.name("Requests/Items Ratio")
class RequestsItemsRatioMonitor(Monitor):
    @monitors.name("Ratio of requests over items scraped count")
    def test_requests_items_ratio(self):
        n_scraped_items = self.data.stats.get("item_scraped_count", 0)
        n_requests_count = self.data.stats.get("downloader/request_count", 0)
        max_ratio = self.data.crawler.settings.get(
            "QUERIDODIARIO_MAX_REQUESTS_ITEMS_RATIO", 5
        )

        if n_scraped_items > 0:
            ratio = n_requests_count / n_scraped_items
            percent = round(ratio * 100, 2)
            allowed_percent = round(max_ratio * 100, 2)
            self.assertLess(
                ratio,
                max_ratio,
                msg=f"""{percent}% is greater than the allowed {allowed_percent}%
                ratio of requests over items scraped.
                """,
            )


class SpiderCloseMonitorSuite(MonitorSuite):

    monitors = [
        RequestsItemsRatioMonitor,
    ]
