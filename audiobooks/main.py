import logging

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from audiobooks.spiders.xzjbzr_spider import XZJBZRSpider

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    settings = get_project_settings()
    # settings.set('FILES_STORE', '/home/ty263/temp/xzjbzr')
    process = CrawlerProcess(settings)
    process.crawl(XZJBZRSpider)

    logger.info("starting ..........")
    process.start()
