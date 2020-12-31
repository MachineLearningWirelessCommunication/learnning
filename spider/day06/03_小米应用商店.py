import json
import time
from pprint import pprint
from threading import Thread
from queue import Queue
# from urllib import parse
import requests, data_headers, pymongo


class XiaomiSpider:
    def __init__(self):
        # 创建空队列
        self.queue = Queue()
        self.url = 'http://app.mi.com/categotyAllListApi?'
        self.product_href_url = 'http://app.mi.com/details?id='
        self.headers = data_headers.headers
        self.conn = pymongo.MongoClient('localhost', 27017)
        self.db = self.conn['im_shop']
        self.myset = self.db['im_info']

    # URL地址入队列
    def url_in(self):
        url = 'http://app.mi.com/details?id='
        pass

    # 线程的事件函数（请求、解析、保存）
    def get_data(self):
        # 从队列中获取URL
        # 发请求，获取响应，提取数据
        for page in range(1,4):
            try:
                url = self.url + 'page ={}& categoryId = 5 & pageSize = 30'.format(str(page))
                res = requests.get(url, headers=self.headers)
                res.encoding = 'utf-8'
                # pprint(json.loads(res.text)['data'])
                produces = json.loads(res.text)['data']
                for product in produces:
                    product_url = self.product_href_url + product['packageName']
                    data = {
                        'product_name': product['displayName'],
                        'product_url': product_url
                    }
                    self.myset.insert_one(data)
                print('第%d页抓取成功！' % page)
                time.sleep(3)
            except Exception as e:
                print(e)

    def main(self):
        # 创建线程
        self.get_data()


if __name__ == '__main__':
    start = time.time()
    spider = XiaomiSpider()
    spider.main()
    end = time.time()
    print('执行时间：%.2f' % (end - start))
