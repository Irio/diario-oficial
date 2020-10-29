BOT_NAME = "gazette"
SPIDER_MODULES = ["gazette.spiders"]
NEWSPIDER_MODULE = "gazette.spiders"
ROBOTSTXT_OBEY = False
ITEM_PIPELINES = {
    "gazette.pipelines.GazetteDateFilteringPipeline": 100,
    "gazette.pipelines.DefaultValuesPipeline": 200,
    "gazette.pipelines.QueridoDiarioFilesPipeline": 300,
    "spidermon.contrib.scrapy.pipelines.ItemValidationPipeline": 400,
    "gazette.pipelines.SQLDatabasePipeline": 500,
}
QUERIDODIARIO_EXTRACT_TEXT_FROM_FILE = True
FILES_STORE = "/mnt/data/"
EXTENSIONS = {
    "spidermon.contrib.scrapy.extensions.Spidermon": 500,
}
SPIDERMON_ENABLED = True
SPIDERMON_VALIDATION_SCHEMAS = ["gazette/schema.json"]
SPIDERMON_VALIDATION_ADD_ERRORS_TO_ITEMS = True
SPIDERMON_VALIDATION_DROP_ITEMS_WITH_ERRORS = True
SPIDERMON_SPIDER_CLOSE_MONITORS = ("gazette.monitors.SpiderCloseMonitorSuite",)

QUERIDODIARIO_DATABASE_URL = "sqlite:///querido-diario.db"
QUERIDODIARIO_MAX_REQUESTS_ITEMS_RATIO = 5
