from time import sleep
import csv

from selenium import webdriver


class JdSpider:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.url = 'http://www.jd.com'

    # 获取商品页面
    def get_page(self):
        self.driver.get(self.url)
        # 查找2个节点
        self.driver.find_element_by_xpath('//*[@id="key"]').send_keys('爬虫书籍')
        self.driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button/i').click()
        sleep(2)
        # self.driver.save_screenshot('京东.png')

    # 解析页面
    def parse_page(self):
        # 把下拉菜单拉倒最下面，让所有商品动态加载出来
        self.driver.execute_script(
            'window.scrollTo(0,document.body.scrollHeight)'
        )
        sleep(3)
        # 找到所有商品信息的节点对象
        # li_list： ['','',...]
        li_list = self.driver.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
        for li in li_list:
            # print(li.text)
            # print('*'*50)
            product_list = li.text.split('\n')  # ['价格'，‘名称’，‘评价’，‘出版社’]
            if product_list[0][:2] == "每满":
                price = product_list[1]
                name = product_list[2]
                commit = product_list[3]
                market = product_list[4]
            elif product_list[0][:2] == "单件":
                price = product_list[3]
                name = product_list[4]
                commit = product_list[5]
                market = product_list[6]
            else:
                price = product_list[0]
                name = product_list[1]
                commit = product_list[2]
                market = product_list[3]
            with open('京东.csv', 'a', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([price, name, commit, market])

    def main(self):
        self.get_page()
        # 控制翻页
        while True:
            self.parse_page()
            # 判断是否为最后一页
            # print(type(self.driver.page_source.find('pn-next disabled')))
            if self.driver.page_source.find('pn-next disabled') == -1:
                self.driver.find_element_by_class_name('pn-next').click()
                sleep(3)
            else:
                break


if __name__ == '__main__':
    jdSpider = JdSpider()
    jdSpider.main()
