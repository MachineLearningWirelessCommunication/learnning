"""电影天堂  抓取
    电影天堂（二级页面）
    1、搜索：电影天堂 - 2019年新片精品 -点击更多
    2、url
    3、正则表达式
    Auth: YZL
"""
from urllib import parse, request
import re, time, random, pymongo
from ver_conf import user_agent

"""
电影天堂首页：/index.htm
点击更多：/html/gndy/dyzz/index.html
"""


class FilmsSkySpider:
    def __init__(self):
        self.__url = 'https://www.dytt8.net'
        self.__indexUrl = "/index.htm"
        # 创建mongodb 连接对象
        self.__conn = pymongo.MongoClient('localhost', 27017)
        # 创建 库对象
        self.__mongo_db = self.__conn['filmSky']
        # self.sleepTime = random.randint(0,3)

    def __get_html(self, url):
        """获取页面"""
        req = request.Request(url, headers=random.choice(user_agent))
        res = request.urlopen(req)
        html = res.read().decode("ANSI","ignore")
        return html

    def __reMatched(self, pattern, html):
        """正则匹配"""
        p = re.compile(pattern, re.S)
        r_list = p.findall(html)
        return r_list

    def __get_filmsIndex(self):
        """
        获取“电影天堂”首页
        :return: “电影天堂”首页
        """
        index_url = self.__url + self.__indexUrl
        index_html = self.__get_html(index_url)
        return index_html

    def __get_clickMore(self, html):
        """
        获取”点击更多“页面
        :param html: ”电影天堂“首页
        :return: ”点击更多“页面
        """
        # 获取”点击更多“的链接地址
        pattern = '<div class="title_all">.*?href="(.*?)">更多>></a>'
        clickMoreUrl_list = self.__reMatched(pattern, html)
        clickMore_url = self.__url + clickMoreUrl_list[0]
        # 发送请求
        clickMore_html = self.__get_html(clickMore_url)
        return clickMore_html, clickMoreUrl_list[0]  # clickMoreUrl_list[0][:-10]   /html/gndy/dyzz/

    def __get_filmshref(self, html):
        """
        获取“点击更多”页面的电影的链接和电影名
        :param html: “点击更多”页面
        :return:
        """
        pattern = '<div class="co_content8">.*?<table.*?<a href="(.*?)" class="ulink">(.*?)</a>.*?</table>'
        filmsUrl_list = self.__reMatched(pattern, html)  # [("",""),("",""),...]
        return filmsUrl_list

    def __writeDate_in_mongodb(self, filmsUrl_list):
        # 创建 集合filmsUrl
        flimsSet = self.__mongo_db['filmsUrl']
        # 插入数据：电影名、电影的url
        for film in filmsUrl_list:
            filmsUrlData = {
                "filmName": film[1].strip(),
                "filmUrl": film[0].strip()  # 具体电影的主页面
            }
            flimsSet.insert_one(filmsUrlData)

    def __saveFilmsUrlForPage(self):
        """
        保存每一页面的电影的url至数据库（MongoDB）
        :return:
        """
        # 获取“电影天堂”首页
        index_html = self.__get_filmsIndex()
        time.sleep(random.randint(0,3))
        print('获取“电影天堂”首页，成功！')
        # 获取“点击更多”页面
        clickMore_html, clickMoreUrl = self.__get_clickMore(index_html)
        time.sleep(random.randint(0,3))
        print("获取“点击更多”页面，成功！")
        indexFilmsUrl_list = self.__get_filmshref(clickMore_html)
        time.sleep(random.randint(0,3))
        print("获取’点击更多‘页面首页电影名和电影url，成功！")
        self.__writeDate_in_mongodb(indexFilmsUrl_list)  # 把首页的电影：电影名和电影Url存储到数据库
        time.sleep(random.randint(0,3))
        print("’点击更多‘页面首页电影名和电影url写入数据库，成功！")
        for page in range(2, 8):  # 2~7页面的电影：电影名和电影Url存储到数据库
            clickMore_url = self.__url + clickMoreUrl[:-10] + 'list_23_%d.html' % page  # 每个页面的地址
            filmsInfo_html = self.__get_html(clickMore_url)
            time.sleep(random.randint(0,3))
            print("获取第%d页，成功！" % page)
            filmsUrl_list = self.__get_filmshref(filmsInfo_html)
            time.sleep(random.randint(0,3))
            print("获取’点击更多‘页面第%d页电影名和电影url，成功！" % page)
            self.__writeDate_in_mongodb(filmsUrl_list)
            time.sleep(random.randint(0,3))
            print("’点击更多‘页面第%d页电影名和电影url写入数据库，成功！" % page)

    def main(self):
        self.__saveFilmsUrlForPage()


if __name__ == '__main__':
    flimSpider = FilmsSkySpider()
    flimSpider.main()
