import csv

# 打开文件
with open('老师.csv', 'a', encoding='utf-8') as f:
    # 初始化写入对象
    writer = csv.writer(f)
    # 对象的writerrow()方法写入数据
    writer.writerow(['韦叔叔', 'Python'])
    writer.writerow(['超叔叔', 'Spider'])
    writer.writerow(['1', '2'])
