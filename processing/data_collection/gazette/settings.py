BOT_NAME = "gazette"
SPIDER_MODULES = ["gazette.spiders"]
NEWSPIDER_MODULE = "gazette.spiders"
ROBOTSTXT_OBEY = False

USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.85 Safari/537.36"
SPLASH_URL = "http://localhost:8050"

ITEM_PIPELINES = {
    "scrapy_splash.SplashCookiesMiddleware": 723,
    "scrapy_splash.SplashMiddleware": 725,
    # "gazette.pipelines.GazetteDateFilteringPipeline": 50,
    # "scrapy.pipelines.files.FilesPipeline": 100,
    # "gazette.pipelines.ExtractTextPipeline": 200,
}

SPIDER_MIDDLEWARES = {
    "scrapy_splash.SplashDeduplicateArgsMiddleware": 100,
}

DUPEFILTER_CLASS = "scrapy_splash.SplashAwareDupeFilter"
HTTPCACHE_STORAGE = "scrapy_splash.SplashAwareFSCacheStorage"

FILES_STORE = "/mnt/data/"
QUERIDODIARIO_EXTRACT_TEXT_FROM_FILE = True
