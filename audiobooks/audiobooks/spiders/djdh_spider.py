from audiobooks.spiders.audiobook_spider import AudiobookSpider

logger = logging.getLogger(__name__)


class DJDHSpider(AudiobookSpider):
    name = "dajangdahe"

    custom_settings = {
        'FILES_STORE': '/home/ty263/temp/djdh/',
    }

    web_url = 'https://www.tingchina.com/yousheng/disp_31046.htm'
    base_url = 'https://t3344.tingchina.com/yousheng/%E5%AE%98%E5%9C%BA%E5%95%86%E6%88%98/%E5%A4%A7%E6%B1%9F%E5%A4%A7%E6%B2%B3/'

    format_string = '{:0>3d}'

    name_len = 3

    _album_name = '大江大河'
