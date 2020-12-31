import requests, time, random
from hashlib import md5


def md5_(string_):
    s = md5()
    s.update(string_.encode())
    return s.hexdigest()


def get_salt_sign_ts_bv(word):
    # 获取ts
    lts = str(int(time.time() * 1000))
    # 获取bv
    User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    bv = md5_(User_Agent)
    # 获取salt
    salt = lts + str(random.randint(0, 9))
    # 获取sign
    sign_string = 'fanyideskweb' + word + salt + '@6f#X3=cCuncYssPsuRUE'
    sign = md5_(sign_string)
    return lts, bv, salt, sign


def attack_yd(word):
    lts, bv, salt, sign = get_salt_sign_ts_bv(word)
    # post 的 url
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    # 定义headers
    headers = {
        # "Accept": "application/json, text/javascript, */*; q=0.01",
        # "Accept-Encoding": "gzip, deflate",
        # "Accept-Language": "zh-CN,zh;q=0.9",
        # "Connection": "keep-alive",
        # "Content-Length": "240",
        # "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=-1391426907@10.169.0.82; JSESSIONID=aaastBh7lNC087pJJ-qwx; OUTFOX_SEARCH_USER_ID_NCOO=381730479.0502364; ___rl__test__cookies=1604456634757",
        #"Host": "fanyi.youdao.com",
        #"Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        #"X-Requested-With": "XMLHttpRequest",
    }
    # 定义data
    data = {
        "i": word,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": sign,
        "lts": lts,
        "bv": bv,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME",
    }
    res = requests.post(url=url, headers=headers, data=data)
    res.encoding = 'utf-8'
    print(res.json())


if __name__ == '__main__':
    word = input("请输入要翻译的单词：")
    attack_yd(word)
