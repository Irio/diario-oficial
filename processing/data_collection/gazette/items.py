import scrapy


class Gazette(scrapy.Item):
    source_text = scrapy.Field()
    date = scrapy.Field()
    edition_number = scrapy.Field()
    file_checksum = scrapy.Field()
    file_path = scrapy.Field()
    file_url = scrapy.Field()
    is_extra_edition = scrapy.Field()
    territory_id = scrapy.Field()
    power = scrapy.Field()
    scraped_at = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
