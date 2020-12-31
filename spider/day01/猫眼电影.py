from pprint import pprint
from time import sleep
from urllib import parse,request
import re

class MaoyanFilmsSpider:
    def __init__(self):
        self.url = "https://maoyan.com/board/4?"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
        }
        # self.d = {}

    def get_page(self,url):
        req = request.Request(url,headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        return html

    # def encode_params(self):
    #     return parse.urlencode(self.d)

    def get_datas(self,html):
        pattern = '<div class="movie-item-info">.*?title="(.*?)" data-act.*?class="star">(.*?)</p>.*?' \
                  'class="releasetime">(.*?)</p>.*?</div>'
        p = re.compile(pattern,re.S)
        r_list = p.findall(html)
        return r_list

    def save_page(self,filename,html):
        with open(filename,'w',encoding='utf-8') as f:
            f.write(html)

    def main(self):
        lst_films = []
        for page in range(1,11):
            offset=(page-1)*10
            filename = "猫眼电影第%d页.html"%page
            Url = self.url + "offset=%d"%offset
            # print(Url)
            html = self.get_page(Url)
            self.save_page(filename,html)
            # sleep(3)
            r_list = self.get_datas(html)
            lst_films.append(r_list)
        return lst_films


if __name__ == '__main__':
    films_spider = MaoyanFilmsSpider()
    pprint(films_spider.main())