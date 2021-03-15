from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


from dajiangdahe.spiders.audiobook_spider import AudiobookSpider
from zipfiles.zipfiles.spiders.NirsoftSpider import NirsoftSpider

if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl(AudiobookSpider)
    # process.crawl(NirsoftSpider)
    process.start()
