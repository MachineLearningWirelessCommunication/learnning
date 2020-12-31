from lxml import etree

html = """
        省略
"""
# 匹配新浪社会
xpath = "//div[@class='wrapper']/a[@id='channel']/text()"
parse_html = etree.HTML(html)
r_list = parse_html.xpath(xpath)
print(r_list)
