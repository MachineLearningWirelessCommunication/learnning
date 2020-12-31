"""库：xxx 集合：xxx"""
import pymongo
database = 'aid1901'
collection = 'student'
# 连接对象
conn = pymongo.MongoClient('localhost', 27017)

# 库对象
# db = conn.aid1901
db = conn[database]

# 集合对象
# myset = db.student
myset = db[collection]

# 插入数据
myset.insert_one(
    {'姓名': '杨中林', '年龄': 27}
)
