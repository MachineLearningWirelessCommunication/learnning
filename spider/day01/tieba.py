from urllib import parse, request


class TiebaSpider:
    def __init__(self):
        self.url = "http://tieba.baidu.com/f?"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
        self.d = {}

    def encode_url(self):
        """
            编译请求参数值
        :return: 编译后的参数值
        """
        params = parse.urlencode(self.d)
        return params

    def get_page(self, url):
        """
        获取页面
        :param url:抓取的地址
        :return: 响应结果
        """
        req = request.Request(url, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        return html

    def parse_page(self):
        """
        解析页面（提取数据）
        :return: 解析后的数据
        """
        pass

    def save_page(self, filename, html):
        """
        保存响应结果至本地文件
        :param filename: 保存后的文件名
        :param html: 要保存的页面
        """
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)

    def main(self):
        """
        抓取贴吧页面的主函数
        """
        name = input("请录入贴吧名：")
        start = int(input("请录入起始页："))
        end = int(input("请录入终止页："))
        self.d['kw'] = name
        for page in range(start, end + 1):
            self.d['pn'] = page
            params = self.encode_url()
            Url = self.url + params
            html = self.get_page(Url)
            filename = "%s吧，第%d页.html" % (name, page)
            self.save_page(filename, html)
            print(filename + ",抓取成功！")


if __name__ == '__main__':
    spider = TiebaSpider()
    spider.main()
