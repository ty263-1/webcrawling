from audiobooks.spiders.audiobook_spider import AudiobookSpider

logger = logging.getLogger(__name__)


class XZJBZRSpider(AudiobookSpider):
    name = "xinzhujingbanzhuren"

    custom_settings = {
        'FILES_STORE': '/home/ty263/temp/xzjbzr/',
    }

    _web_url = 'https://www.tingchina.com/yousheng/disp_31009.htm'

    _base_url = 'https://t3344.tingchina.com/yousheng/%E5%AE%98%E5%9C%BA%E5%95%86%E6%88%98/%E5%AF%B9%E6%89%8B%E4%B8%8A%E9%83%A8-%E6%96%B0%E9%A9%BB%E4%BA%AC%E5%8A%9E%E4%B8%BB%E4%BB%BB/'

    _format_string = '{:0>4d}'

    _name_len = 4

    _album_name = '新驻京办主任'

    @property
    def base_url(self):
        return self._base_url

    @base_url.setter
    def base_url(self, value):
        self._base_url = value

    # @property
    # def format_string(self):
    #     return self._format_string
    #
    # @x.setter
    # def format_string(self, value):
    #     self._format_string = value

    @property
    def name_len(self):
        return self._name_len

    @name_len.setter
    def name_len(self, value):
        self._name_len = value

    @property
    def web_url(self):
        return self._web_url

    @web_url.setter
    def web_url(self, value):
        self._web_url = value

    @property
    def album_name(self):
        return self._album_name

    @album_name.setter
    def album_name(self, value):
        self._album_name = value
