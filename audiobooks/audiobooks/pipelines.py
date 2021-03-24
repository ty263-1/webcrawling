# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os

import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline
from scrapy.utils.project import get_project_settings
import mutagen
from mutagen.mp3 import MP3, EasyMP3


class DajiangdahePipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        file_name: str = request.url.split("/")[-1][:7]
        return file_name

    # def get_media_requests(self, item, info):
    #     print('22222222222222222222222222222222222')
    #     adapter = ItemAdapter(item)
    #     for file_url in adapter['file_urls']:
    #         yield scrapy.Request(file_url)

    def item_completed(self, results, item, info):
        storage_dir = get_project_settings().get('FILES_STORE')
        file_name = [x['path'] for ok, x in results if ok]
        audio = EasyMP3(os.path.join(storage_dir, file_name[0]))
        audio["title"] = file_name
        audio["artist"] = '读客熊猫君'
        audio["album"] = '大江大河'
        audio["genre"] = ''
        audio.pprint()
        audio.save()

        return item

