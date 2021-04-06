# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import logging
import os

import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline
from scrapy.utils.project import get_project_settings
import mutagen
from mutagen.mp3 import EasyMP3

logger = logging.getLogger(__name__)


class AudiobookItemPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        file_name: str = request.url.split("/")[-1][:7]
        return file_name

    # def get_media_requests(self, item, info):
    #     print('22222222222222222222222222222222222')
    #     adapter = ItemAdapter(item)
    #     for file_url in adapter['file_urls']:
    #         yield scrapy.Request(file_url)

    def item_completed(self, results, item, info):
        # storage_dir = get_project_settings().get('FILES_STORE')
        storage_dir = self.crawler.settings.get('FILES_STORE')
        file_name = [x['path'] for ok, x in results if ok]
        try:
            audio = EasyMP3(os.path.join(storage_dir, file_name[0]))
        except IndexError:
            logger.debug(file_name)
        audio["title"] = file_name
        audio["artist"] = item['artist_name']
        audio["album"] = item['album_name']
        audio["genre"] = ''
        audio.pprint()
        audio.save()

        return item
