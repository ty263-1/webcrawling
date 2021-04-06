from abc import abstractmethod, ABC

import scrapy
import re

from scrapy import Request

from audiobooks.items import AudiobookItem


class AudiobookSpider(scrapy.Spider, ABC):
    name = "audiobook"

    # web_url = 'https://www.tingchina.com/yousheng/disp_31046.htm'
    # base_url = 'https://t3344.tingchina.com/yousheng/%E5%AE%98%E5%9C%BA%E5%95%86%E6%88%98/%E5%A4%A7%E6%B1%9F%E5%A4%A7%E6%B2%B3/'
    h5_jsonp_url = 'https://img.tingchina.com/play/h5_jsonp.asp?0.11683375963617659'

    audiobook_dict = {}

    retry_list = []

    key_string = ''

    start_episode_number = 75

    def start_requests(self):
        yield Request.from_curl(
                    "curl 'https://img.tingchina.com/play/h5_jsonp.asp?0.11683375963617659' \
                      -H 'Connection: keep-alive' \
                      -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36' \
                      -H 'Accept: */*' \
                      -H 'Sec-Fetch-Site: same-site' \
                      -H 'Sec-Fetch-Mode: no-cors' \
                      -H 'Sec-Fetch-Dest: script' \
                      -H 'Referer: https://www.tingchina.com/yousheng/31046/play_31046_0.htm' \
                      -H 'Accept-Language: en-US,en;q=0.9' \
                      -H 'Cookie: UM_distinctid=177461d45ea7fc-09f21ff66496a9-1e2a1f04-25a3ac-177461d45eb6a8; ting_0_31046_1=0; ting_0_31046_2=490.593481; tingNewJieshaoren=0; ASPSESSIONIDSGTTAATQ=OKMJNKKBJGNBGGHLGNPFKAHM; tingNewIP%2D0%2D31046=over; tNew_play_url=https%3A//www.tingchina.com/yousheng/31046/play_31046_0.htm; ting_0_31046_0=430.00254; cscpvrich2729_p=1' \
                      --compressed",
                    callback=self.parse_key_string
                )

    # def parse(self, response):
    #     if response.status == 404:
    #         self.retry_list.append(response.url)
    #         return
    #
    #     yield from response.follow_all(css='div.list ul li a', callback=self.parse)

    def parse_key_string(self, response):
        p = re.compile('key=(.*)";')
        result = p.search(response.text)
        self.key_string = result.group(1)

        yield scrapy.Request(self.web_url, self.parse)

    def parse(self, response, **kwargs):
        episode_number = len(response.css("div.list ul li a").getall())

        for i in range(self.start_episode_number, episode_number + 1):
            index = str(i).rjust(self.name_len, '0')
            audiobook_url = self.base_url + index + '.mp3' + '?key=' + self.key_string
            self.audiobook_dict[index] = audiobook_url

        for key, value in self.audiobook_dict.items():
            item = AudiobookItem()
            item['file_urls'] = [value]
            item['album_name'] = self.album_name
            item['artist_name'] = ''
            yield item

    @property
    @abstractmethod
    def base_url(self):
        raise NotImplementedError()

    @base_url.setter
    @abstractmethod
    def base_url(self, value):
        raise NotImplementedError()

    @property
    @abstractmethod
    def name_len(self):
        raise NotImplementedError()

    @name_len.setter
    @abstractmethod
    def name_len(self, value):
        raise NotImplementedError()

    @property
    @abstractmethod
    def web_url(self):
        raise NotImplementedError()

    @web_url.setter
    @abstractmethod
    def web_url(self, value):
        raise NotImplementedError()

    @property
    @abstractmethod
    def album_name(self):
        raise NotImplementedError()

    @album_name.setter
    @abstractmethod
    def album_name(self, value):
        raise NotImplementedError()
