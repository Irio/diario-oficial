import datetime as dt
import os
import subprocess
from pathlib import Path

import magic
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.http import Request
from scrapy.pipelines.files import FilesPipeline
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from gazette.database.models import initialize_database, Gazette
from gazette.settings import FILES_STORE


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


class ExtractTextPipeline:
    """
    Identify file format and call the right tool to extract the text from it
    """

    def process_item(self, item, spider):
        extract_text_from_file = spider.settings.getbool(
            "QUERIDODIARIO_EXTRACT_TEXT_FROM_FILE", True
        )
        if not extract_text_from_file:
            return item

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

        return item

    def pdf_source_text(self, item):
        """
        Gets the text from pdf files
        """
        pdf_path = os.path.join(FILES_STORE, item["files"][0]["path"])
        text_path = pdf_path + ".txt"
        command = f"pdftotext -layout {pdf_path} {text_path}"
        subprocess.run(command, shell=True, check=True)
        with open(text_path) as file:
            return file.read()

    def doc_source_text(self, item):
        """
        Gets the text from docish files
        """
        doc_path = os.path.join(FILES_STORE, item["files"][0]["path"])
        text_path = doc_path + ".txt"
        command = f"java -jar /tika-app.jar --text {doc_path}"
        with open(text_path, "w") as f:
            subprocess.run(command, shell=True, check=True, stdout=f)
        with open(text_path, "r") as f:
            return f.read()

    def txt_source_text(self, item):
        """
        Gets the text from txt files
        """
        with open(
            os.path.join(FILES_STORE, item["files"][0]["path"]), encoding="ISO-8859-1"
        ) as f:
            return f.read()

    def is_pdf(self, filepath):
        """
        If the file type is pdf returns True. Otherwise,
        returns False
        """
        return self._is_file_type(filepath, file_types=["application/pdf"])

    def is_doc(self, filepath):
        """
        If the file type is doc or similar returns True. Otherwise,
        returns False
        """
        file_types = [
            "application/msword",
            "application/vnd.oasis.opendocument.text",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        ]
        return self._is_file_type(filepath, file_types)

    def is_txt(self, filepath):
        """
        If the file type is txt returns True. Otherwise,
        returns False
        """
        return self._is_file_type(filepath, file_types=["text/plain"])

    def get_file_type(self, filename):
        """
        Returns the file's type
        """
        file_path = os.path.join(FILES_STORE, filename)
        return magic.from_file(file_path, mime=True)

    def _is_file_type(self, filepath, file_types):
        """
        Generic method to check if a identified file type matches a given list of types
        """
        return self.get_file_type(filepath) in file_types


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

        session = self.Session()

        item_file = item["files"][0]
        item["file_path"] = item_file["path"]
        item["file_url"] = item_file["url"]
        item["file_checksum"] = item_file["checksum"]
        item.pop("files")
        item.pop("file_urls")

        gazette = Gazette(**item)
        try:
            session.add(gazette)
            session.commit()
        except IntegrityError:
            spider.logger.warning(
                f"Gazette from {item['date']} already exists in the database."
            )
            session.rollback()
        except Exception:
            session.rollback()
            raise

        finally:
            session.close()

        return item


class RequestWithItem(Request):
    """
    Specialized Request object to allow carry the item which generate the request.
    Thus, we can use the gazette date in the path where the file will be stored.
    """

    def __init__(self, url, item):
        super().__init__(url)
        self.item = item


class QueridoDiarioFilesPipeline(FilesPipeline):
    """
    When the downloaded file are stored in a remote storage system (e.g.
    Digital Ocean spaces), we need to specialize FilesPipeline class in order
    to allow us define a different directory where the files will be store. In
    the current implementation we organize gazette files by date. All the
    gazettes from the same date will be store in the same directory.
    """

    def file_path(self, request, response=None, info=None):
        filepath = super().file_path(request, response, info)
        # The default path from the scrapy class begins with "full/". In this
        # class we replace that with the gazette date.
        datestr = request.item["date"].strftime("%d-%m-%Y")
        filename = Path(filepath).name
        return str(Path(datestr, filename))

    def get_media_requests(self, item, info):
        urls = ItemAdapter(item).get(self.files_urls_field)
        if not urls:
            return
        yield from (RequestWithItem(u, item) for u in urls)
