# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from .settings import *


class MaoyanPipeline:
    def process_item(self, item, spider):
        print('*' * 50)
        print(dict(item))
        print('*' * 50)
        # 必须返回item，传递给下一个管道的process_item()
        return item


# 新建MongoDB管道类
class MaoyanMongoPipeline:
    # def __init__(self):
    #     pass

    # 爬虫开始执行时，执行此函数（只执行一次）
    def open_spider(self, spider):
        # 连接对象
        self.conn = pymongo.MongoClient(MONGO_HOST,MONGO_PORT)
        # 库对象
        self.db = self.conn[MONGO_DB]
        # 集合对象
        self.myset = self.db[MONGO_SET]

    def process_item(self, item, spider):
        data = {
            'name': item['name'],
            'star': item['star'],
            'time': item['time']
        }
        self.myset.insert_one(data)
        return item

    # 爬虫结束时，执行次函数（只执行一次）
    def close_spider(self, spider):
        pass
