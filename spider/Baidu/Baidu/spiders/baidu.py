import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'  # 爬虫名
    allowed_domains = ['baidu.com']  # 允许爬取的域名
    start_urls = ['http://www.baidu.com/']  # 起始的url地址

    def parse(self, response):
        print(response.text)
