import scrapy


class Gazette(scrapy.Item):
    source_text = scrapy.Field()
    date = scrapy.Field()
    file_checksum = scrapy.Field()
    file_path = scrapy.Field()
    file_url = scrapy.Field()
    is_extra_edition = scrapy.Field()
    territory_id = scrapy.Field()
    power = scrapy.Field()
    scraped_at = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
    # TEMP: Can be removed once this attribute stop being used.
    #       Check PostgreSQLPipeline for more info.
    municipality_id = scrapy.Field()

    """This field is consumed by gazette.pipelines.SessionAwareFilesPipeline.
    It's intent is to provide a way to fetch files when the URL alone is
    not enough, i.e. you need a specific session (cookiejar) and/or form
    parameters, this often happens with component-based server-side frameworks
    like Java Server Faces. The supported value is a list with dictionaries.
    Each entry must have the following attributes:
    
    - url: the URL to fetch the file from
    - formdata: a dictionary with values to be passed
    - cookiejar: the unique id of the cookiejar to use for the download request

    This field is popped out after being consumed, i.e. it is not stored in the
    database. Example usage: gazette.spiders.sp_ribeirao_preto.SpRibeiraoPretoSpider
    """
    file_requests = scrapy.Field()
