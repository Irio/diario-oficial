BOT_NAME = "gazette"
SPIDER_MODULES = ["gazette.spiders"]
NEWSPIDER_MODULE = "gazette.spiders"
ROBOTSTXT_OBEY = False
ITEM_PIPELINES = {
    "scrapy.pipelines.files.FilesPipeline": 100,
    "gazette.pipelines.ExtractTextPipeline": 200,
}
SPIDER_MIDDLEWARES = {
    "gazette.middlewares.GazetteDateFilteringSpiderMiddleware": 0,
}
FILES_STORE = "/mnt/data/"
QUERIDODIARIO_EXTRACT_TEXT_FROM_FILE = True
