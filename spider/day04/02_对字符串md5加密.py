from hashlib import md5

St = '626539yang'

# 对字符串加密
# 1、创建加密对象
s = md5()
# 2、进行加密，参数一定为bytes类型
s.update(St.encode())
# 3、获取十六进制的加密结果
res = s.hexdigest()

print(res)

# QQkTVH0fr4CGfnD7aCmAyPqmhTqQT5d%2FoLTHkV2SqsqhIbsN1DIaW54HWjd%2BvpMu0KTqlpcJfBhz5FQLlgmGewjpjIjSaOEMTbIDHDflmONl%2Bexf
# EkJjI604pG7xc7UFsySfyhQzLmVGfpJU9laeP%2B3Ars2p%2FPuYIn2Soz1IgJQ%3D