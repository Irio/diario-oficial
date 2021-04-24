import pkg_resources

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

DOWNLOAD_TIMEOUT = 360

FILES_STORE = "s3://queridodiariobucket/"
MEDIA_ALLOW_REDIRECTS = True

EXTENSIONS = {
    "spidermon.contrib.scrapy.extensions.Spidermon": 500,
    "gazette.extensions.StatsPersist": 600,
}
SPIDERMON_ENABLED = True
SPIDERMON_VALIDATION_SCHEMAS = [
    pkg_resources.resource_filename("gazette", "resources/gazette_schema.json")
]

SPIDERMON_VALIDATION_ADD_ERRORS_TO_ITEMS = True
SPIDERMON_VALIDATION_DROP_ITEMS_WITH_ERRORS = True
SPIDERMON_SPIDER_CLOSE_MONITORS = ("gazette.monitors.SpiderCloseMonitorSuite",)
SPIDERMON_MAX_ERRORS = 0

SPIDERMON_TELEGRAM_FAKE = True
SPIDERMON_TELEGRAM_SENDER_TOKEN = "<TELEGRAM_BOT_TOKEN>"
SPIDERMON_TELEGRAM_RECIPIENTS = ["<RECIPIENT>"]

QUERIDODIARIO_DATABASE_URL = "postgresql://queridodiario:queridodiario@localhost/queridodiariodb"
QUERIDODIARIO_MAX_REQUESTS_ITEMS_RATIO = 5
QUERIDODIARIO_MAX_DAYS_WITHOUT_GAZETTES = 5

# These settings are needed only when storing downloaded files
# in a S3 bucket
AWS_ACCESS_KEY_ID = "minio-access-key"
AWS_SECRET_ACCESS_KEY = "minio-secret-key"
AWS_ENDPOINT_URL = "http://127.0.0.1:9000"
AWS_REGION_NAME = "us-east-1"
FILES_STORE_S3_ACL = "public-read"
