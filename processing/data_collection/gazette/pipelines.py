import os
import subprocess
from uuid import uuid4

from database.models import Gazette, initialize_database
from scrapy.exceptions import DropItem
from scrapy.pipelines.files import FilesPipeline
from scrapy.http import FormRequest
from sqlalchemy.orm import sessionmaker


from gazette.settings import FILES_STORE


class PdfParsingPipeline:

    def process_item(self, item, spider):
        item['source_text'] = self.pdf_source_text(item)
        for key, value in item['files'][0].items():
            item[f'file_{key}'] = value
        item.pop('files')
        if 'file_urls' in item:
            item.pop('file_urls')
        return item

    def pdf_source_text(self, item):
        pdf_path = os.path.join(FILES_STORE, item['files'][0]['path'])
        command = f'pdftotext -layout {pdf_path}'
        subprocess.run(command, shell=True, check=True)
        if '.pdf' in pdf_path:
            text_path = pdf_path.replace('.pdf', '.txt')
        else:
            text_path = pdf_path + '.txt'
        with open(text_path) as file:
            return file.read()


class PostgreSQLPipeline(object):

    def __init__(self):
        engine = initialize_database()
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        # TEMP: The attribute "municipality_id" was recently renamed to "territory_id"
        #       in the database. The two following lines may be deleted once we have
        #       no branches using "municipality_id".
        if 'municipality_id' in item:
            item['territory_id'] = item.pop('municipality_id')
        gazette = Gazette(**item)
        try:
            session.add(gazette)
            session.commit()
        except:
            session.rollback()
            raise

        finally:
            session.close()
        return item


class GazetteDateFilteringPipeline(object):

    def process_item(self, item, spider):
        if hasattr(spider, 'start_date'):
            if spider.start_date > item.get('date'):
                raise DropItem(
                    'Droping all items before {}'.format(spider.start_date))
        return item


class SessionAwareFilesPipeline(FilesPipeline):
    """This item pipeline adds new behavior to the default
    FilesPipeline provided by Scrapy.

    In some cases we need to pass form data and use
    a specific session (cookiejar) to be able to
    download a gazette file. This often happens with
    component-based server-side libraries like Java
    Server Faces. This custom item pipeline provides a
    way to customize a download request.

    Note that a UUID is generated and used as file_path
    because we can't rely anymore on the request URL to
    determine the file name (because they will be equal).
    Also note that this file_path override only applies to
    the customized requests.

    Example usage: gazette.spiders.sp_ribeirao_preto.SpRibeiraoPretoSpider
    """

    def get_media_requests(self, item, info):
        requests = super().get_media_requests(item, info)
        if 'file_requests' in item:
            for request in item['file_requests']:
                file_path_override = str(uuid4())
                requests.append(FormRequest(request['url'],
                                            formdata=request['formdata'],
                                            meta={'cookiejar': request['cookiejar'],
                                                  'file_path_override': file_path_override}))
            item.pop('file_requests')
        return requests

    def file_path(self, request, response=None, info=None):
        return (
            f'full/{request.meta["file_path_override"]}'
            if 'file_path_override' in request.meta
            else super().file_path(request, response, info)
        )
