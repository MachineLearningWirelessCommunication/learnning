"""库：maoyandb  表： top100 """
import pymysql

# 创建库
# create database maoyandb charset utf8;
# 创建表
# create table top100(
#   name varchar(50),
#   star varchar(300),
#   time varchar(20)
# )charset=utf8;

name = "霸王别姬"
star = "张国荣"
time = "1999"
# 创建数据库连接对象
db = pymysql.connect(
    'localhost',
    'root',
    '123456',
    'maoyandb',
    charset='utf8'
)
# 创建游标对象 cursor
cursor = db.cursor()
# 执行sql命令
sql = 'insert into top100 values(%s,%s,%s)'
cursor.execute(sql, [name, star, time])
# 提交到数据库执行  commit()
db.commit()
# 关闭游标对象、数据库对象
cursor.close()
db.close()
