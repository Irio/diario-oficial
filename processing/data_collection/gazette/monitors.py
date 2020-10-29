from spidermon import Monitor, MonitorSuite, monitors
from spidermon.contrib.actions.telegram import SendTelegramMessage
from spidermon.contrib.scrapy.monitors import (
    ErrorCountMonitor,
    FinishReasonMonitor,
    ItemValidationMonitor,
)


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


class CustomSendTelegramMessage(SendTelegramMessage):
    def get_message(self):
        stats = self.data.stats

        failures = len(self.result.failures)
        emoji = "\U0001F525" if failures > 0 else "\U0001F60E"

        message = "\n".join(
            [
                f"*{self.data.spider.name}* {stats['finish_reason']}",
                f"- Finish time: *{stats['finish_time']}*",
                f"- Gazettes scraped: *{stats['item_scraped_count']}*",
                f"- {emoji} {failures} failures {emoji}",
            ]
        )
        return message


class SpiderCloseMonitorSuite(MonitorSuite):

    monitors = [
        RequestsItemsRatioMonitor,
        ErrorCountMonitor,
        FinishReasonMonitor,
        ItemValidationMonitor,
    ]

    monitors_finished_actions = [CustomSendTelegramMessage]
