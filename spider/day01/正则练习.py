import re

html = """
<div class="animal">
    <p class="name">
        <a title="Tiger"></a>
    </p>
    <p class="content">
        Two Tigers Two Tigers run fast 
    </p>
</div>
<div class="animal">
    <p class="name">
        <a title="Rabbit"></a>
    </p>
    <p class="content">
        Small white rabbit white and white  
    </p>
</div>
"""
pattern = '<div class="animal".*?title="(.*?)"></a>.*?class="content">(.*?)</p>.*?</div>'
p = re.compile(pattern,re.S)
r_list = p.findall(html)
# print(r_list)
for tuple_ in r_list:
    print("动物名称：%s"%tuple_[0])
    print("动物描述：%s"%tuple_[1].strip())
    print("******************************")