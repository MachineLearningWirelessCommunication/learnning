import re
html = """
<div><p>九霄龙吟惊天变</p></div>
<div><p>风云际云潜水游</p></div>
"""


# 贪婪匹配
# pattern = "<div><p>.*</p></div>"

# 非贪婪匹配(爬虫专用)
# pattern = "<div><p>.*?</p></div>"
pattern = "<div><p>(.*?)</p></div>"
p = re.compile(pattern,re.S)
r_list = p.findall(html)
print(r_list)