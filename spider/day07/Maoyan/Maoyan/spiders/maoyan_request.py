import scrapy
from ..items import MaoyanItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan2'
    allowed_domains = ['maoyan.com']
    # 起始的urL地址
    # start_urls = ['https://maoyan.com/board/4?offset=0']
    offset = 0

    # 重写start_requests 方法
    def start_requests(self):
        for offset in range(0, 91, 10):
            url = 'https://maoyan.com/board/4?offset={}'.format(str(offset))
            # 扔到调度器入队列
            yield scrapy.Request(
                url=url,
                callback=self.parse_film
            )

    def __get_value(self, dd, xpath):
        return dd.xpath(xpath).extract()[0].strip()
        # return dd.xpath(xpath).extract_first().strip()
        # return dd.xpath(xpath).get().strip()

    def parse_film(self, response):
        xpath_base = '//*[@id="app"]/div/div/div[1]/dl/dd'  # 基准(电影列表)
        xpath_filmName = './div/div/div[1]/p[1]/a/text()'  # 电影名称
        xpath_filmStar = './div/div/div[1]/p[2]/text()'  # 电影主演
        xpath_fileTime = './div/div/div[1]/p[3]/text()'  # 电影上映时间
        dd_list = response.xpath(xpath_base)
        # 依次遍历
        for dd in dd_list:
            item = MaoyanItem()
            item['name'] = self.__get_value(dd, xpath_filmName)  # extract()
            item['star'] = self.__get_value(dd, xpath_filmStar)
            item['time'] = self.__get_value(dd, xpath_fileTime)
            # print(item)
            yield item