BOT_NAME = 'gazette'
SPIDER_MODULES = ['gazette.spiders']
NEWSPIDER_MODULE = 'gazette.spiders'
ROBOTSTXT_OBEY = False
ITEM_PIPELINES = {
    'gazette.pipelines.GazetteDateFilteringPipeline': 50,
    'gazette.parser.GazetteFilesPipeline': 60,
    'gazette.pipelines.SessionAwareFilesPipeline': 100,
    'gazette.pipelines.PdfParsingPipeline': 200,
    'gazette.pipelines.PostgreSQLPipeline': 300,
}
FILES_STORE = '/mnt/data/'
