import requests

url = "http://www.baidu.com/s?"
params = {
    '':"",
}
headers = {
    '':''
}
res = requests.get(url,params=params,headers=headers)
