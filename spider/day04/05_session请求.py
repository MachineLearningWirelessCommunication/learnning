from requests import session



url = "http://project.unionbigdata.com:82/Home/Login"
headers = {
    "Host": "project.unionbigdata.com:82",
    "Connection": "keep-alive",
    #"Content-Length": "262",
    "Accept": "*/*",
    #"X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "http://project.unionbigdata.com:82",
    "Referer": "http://project.unionbigdata.com:82/Home/Login",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    #"Cookie": "ASP.NET_SessionId=n5vzdra0k5hala5jiobvemnr",
}
data = {
    'UserId':'SZL451',
    'Password':'626539yang'
}
session = session()
session.post(url,data=data,headers=headers)
url_ = "http://project.unionbigdata.com:82/Users/UserHome/Index"
res = session.get(url_,headers=headers)
res.encoding = 'utf-8'
print(res.text)