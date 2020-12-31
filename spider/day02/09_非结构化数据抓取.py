import requests

url = "https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=161517786,2233409295&fm=26&gp=0.jpg"
headers = {'User-Agent':"Mozilla/5.0"}
filename = "非结构化数据抓取之赵丽颖图片.jpg"
res = requests.get(url,headers=headers)
if res.status_code == '200':
    res.encoding = "utf-8"
    res = res.content
    with open(filename,'wb') as f:
        f.write(res)


