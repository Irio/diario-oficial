import datetime as dt
from pathlib import Path

from gazette.database.models import Gazette, initialize_database
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.http import Request
from scrapy.pipelines.files import FilesPipeline
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker


class GazetteDateFilteringPipeline:
    def process_item(self, item, spider):
        if hasattr(spider, "start_date"):
            if spider.start_date > item.get("date"):
                raise DropItem("Droping all items before {}".format(spider.start_date))
        return item


class DefaultValuesPipeline:
    """ Add defaults values field, if not already set in the item """

    default_field_values = {
        "territory_id": lambda spider: getattr(spider, "TERRITORY_ID"),
        "scraped_at": lambda spider: dt.datetime.utcnow(),
    }

    def process_item(self, item, spider):
        for field in self.default_field_values:
            if field not in item:
                item[field] = self.default_field_values.get(field)(spider)
        return item


class SQLDatabasePipeline:
    def __init__(self, database_url):
        self.database_url = database_url

    @classmethod
    def from_crawler(cls, crawler):
        database_url = crawler.settings.get("QUERIDODIARIO_DATABASE_URL")
        return cls(database_url=database_url)

    def open_spider(self, spider):
        if self.database_url is not None:
            engine = initialize_database(self.database_url)
            self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        if self.database_url is None:
            return item

<<<<<<< HEAD
        session = self.Session()
=======
        if self.is_doc(item["files"][0]["path"]):
            item["source_text"] = self.doc_source_text(item)
        elif self.is_pdf(item["files"][0]["path"]):
            item["source_text"] = self.pdf_source_text(item)
        elif self.is_txt(item["files"][0]["path"]):
            item["source_text"] = self.txt_source_text(item)
        else:
            raise Exception(
                "Unsupported file type: " + self.get_file_type(item["files"][0]["path"])
            )

        item_file = item["files"][0]
        if item_file.get("path", None) is not None:
            item["file_path"] = item_file["path"]
        if item_file.get("url", None) is not None:
            item["file_url"] = item_file["url"]
        if item_file.get("checksum", None) is not None:
            item["file_checksum"] = item_file["checksum"]
        if item.get("files", None) is not None:
            item.pop("files")
        if item.get("file_irls", None) is not None:
            item.pop("file_urls")
        return item
>>>>>>> a86454ec94750e94e39aacae482557b4909b1b03

        fields = [
            "source_text",
            "date",
            "edition_number",
            "is_extra_edition",
            "power",
            "scraped_at",
            "territory_id",
        ]
        gazette_item = {field: item.get(field) for field in fields}

        for file_info in item.get("files", []):
            gazette_item["file_path"] = file_info["path"]
            gazette_item["file_url"] = file_info["url"]
            gazette_item["file_checksum"] = file_info["checksum"]

            gazette = Gazette(**gazette_item)
            session.add(gazette)
            try:
                session.commit()
            except IntegrityError:
                spider.logger.warning(
                    f"Gazette already exists in database. "
                    f"Date: {gazette_item['date']}. "
                    f"File Checksum: {gazette_item['file_checksum']}"
                )
                session.rollback()
            except Exception:
                session.rollback()
                raise

        session.close()
        return item


class QueridoDiarioFilesPipeline(FilesPipeline):
    """
    Specialize the Scrapy FilesPipeline class to organize the gazettes in directories.
    The files will be under <territory_id>/<gazette date>/.
    """

    def file_path(self, request, response=None, info=None, item=None):
        filepath = super().file_path(request, response=response, info=info, item=item)
        # The default path from the scrapy class begins with "full/". In this
        # class we replace that with the territory_id and gazette date.
        datestr = item["date"].strftime("%Y-%m-%d")
        filename = Path(filepath).name
        return str(Path(item["territory_id"], datestr, filename))
