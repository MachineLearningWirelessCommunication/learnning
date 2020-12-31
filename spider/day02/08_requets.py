import requests

url = "http://www.baidu.com/"
headers = {'User-Agent': "Mozilla/5.0"}

# 向百度发起请求，并得到响应对象
res = requests.get(url, headers=headers)
# 获取响应内容(字符串)
print(res.encoding)
res.encoding = "utf-8"  #
html = res.text
# 获取bytes数据类型
Html = res.content
# 获取http响应码
statusCode = res.status_code
print(statusCode)
# 获取返回数据的url地址 （重定向后的地址）
URL = res.url
print(URL)
