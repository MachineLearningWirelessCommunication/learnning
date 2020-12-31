import os

from flask import Flask, render_template

# 创建一个Flask的程序实例，以便接收用户的请求和响应
# 要将当前运行的模块文件作为Flask的程序实例
app = Flask(__name__)


# @app.route(''): 路由定义，用于匹配用户的访问路径
# def index():  匹配上路由之后要执行的操作函数   -  视图函数
@app.route('/index')
def index():
    return 'Hello World'


# 带多个参数的路由
@app.route('/show/<name>/<age>')
def show(name, age):
    # name 表示的就是路由中的name参数值
    # age 表示的就是路由中的age参数值
    print("name:", name)
    print("age:", age)
    return "接收数据成功！"


# 带多个参数的路由
@app.route('/calculate/<data1>/<data2>')
def calculate(data1, data2):
    """
        将传递进来的两个参数做 四则运算
        将结果响应给 客户浏览器
    """
    data1 = int(data1)
    data2 = int(data2)
    response = "%d + %d = %d" % (data1, data2, data1 + data2) + '<br>'
    response += "%d - %d = %d" % (data1, data2, data1 - data2) + '<br>'
    response += "%d * %d = %d" % (data1, data2, data1 * data2) + '<br>'
    response += "%d / %d = %d" % (data1, data2, data1 / data2) + '<br>'
    response += "%d %% %d = %d" % (data1, data2, data1 % data2) + '<br>'
    return response


# 指定参数类型的路由
"""
    类型转换器     作用
    缺省          字符串，不能包含  /
    int:         整数
    float:       浮点数
    path:        字符串，允许包含  /
"""


@app.route('/typeChange/<int:data1>/<int:data2>')
def typeChange(data1, data2):
    response = "%d + %d = %d" % (data1, data2, data1 + data2) + '<br>'
    response += "%d - %d = %d" % (data1, data2, data1 - data2) + '<br>'
    response += "%d * %d = %d" % (data1, data2, data1 * data2) + '<br>'
    response += "%d / %d = %d" % (data1, data2, data1 / data2) + '<br>'
    response += "%d %% %d = %d" % (data1, data2, data1 % data2) + '<br>'
    return response


# 多url的路由匹配：多个访问地址最终匹配到同一个视图处理函数
@app.route('/')
@app.route('/showIndex')
@app.route('/showIndex/1')
def showIndex():
    return "这是首页！"


# 模板
@app.route('/temp')
def temp():
    # 默认情况下，Flask会到项目中找到一个templates的文件夹，去搜索要用到的
    # path = os.path.dirname(__file__)+"t"
    return render_template('temp.html')


if __name__ == '__main__':
    # app.run(): 启动Flask 的服务   默认端口5000
    app.run('localhost', 5000, debug=True)
