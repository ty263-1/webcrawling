from audiobooks.spiders.audiobook_spider import AudiobookSpider


class XZJBZRSpider(AudiobookSpider):
    name = "xzjbzr"

    web_url = 'https://www.tingchina.com/yousheng/disp_31046.htm'
    base_url = 'https://t3344.tingchina.com/yousheng/%E5%AE%98%E5%9C%BA%E5%95%86%E6%88%98/%E5%A4%A7%E6%B1%9F%E5%A4%A7%E6%B2%B3/'

