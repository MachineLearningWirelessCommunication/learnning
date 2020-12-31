from flask import Flask, render_template,request

app = Flask(
            __name__,
            template_folder='t',
            static_folder='s',
            static_url_path='/s'
            )


@app.route('/01-var')
def var():
    return render_template('01-var.html', name='yzl', age=27)


@app.route('/02-varexer')
def varexer():
    return render_template('02-varexer.html',
                           groupName='<<保健三人组>>',
                           groupLeader='老魏',
                           TeamMembers01='吕泽',
                           TeamMembers02='王丹')


@app.route('/02-var')
def var02():
    # 字符串
    name = 'yzl'
    # 数值
    age = 27
    # 列表
    lst = ['good', 'perfect', 'well']
    # 元组
    tup = ('好', '很好', '非常好')
    # 字典
    dic = {
        '姓名': 'yzl',
        '年龄': 27
    }
    dog = Animal()
    dog.name = '拉布拉多'
    # return render_template(
    #     '02-var.html',
    #     name=name,
    #     age = age,
    #     lst = lst,
    #     tup = tup,
    #     dic= dic,
    #     dogName = dog.name
    # )
    return render_template(
        '02-var.html',
        params=locals()
    )


class Animal:
    name = None


@app.route('/03-for')
def forViews():
    lst = [
        {
            'name': '老魏',
            'age': 44,
            'gender': '男',
        },
        {
            'name': '波波',
            'age': 36,
            'gender': '男'
        },
        {
            'name': '小泽Maria',
            'age': 30,
            'gender': '男'
        },
        {
            'name': '赵丽颖',
            'age': 18,
            'gender': '女'
        }
    ]
    return render_template('03-forViews.html', lst=lst)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
