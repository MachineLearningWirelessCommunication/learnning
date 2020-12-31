import os
from flask import Flask, render_template, request,redirect
from util import util
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy import or_, func

app = Flask(__name__)
# pymysql.install_as_MySQLdb()
# 指定数据库的配置信息，连接到flaskDB的数据库上
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456' \
                                        '@172.27.28.50:3306/flaskdb'

# 指定信号追踪
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 配置自动提交操作回数据库
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# 创建SQLALchemy的示例  -- db   用于做数据库的操作
db = SQLAlchemy(app)
print(db)

# 创建Manager实例 并指定要管理哪个app
manager = Manager(app)
# 创建Migrate 对象   并指定要关联的app和db
migrate = Migrate(app, db)
# 为manager 增加数据迁移的子命令
manager.add_command('db', MigrateCommand)

"""
    创建实体类 - Users  映射到数据库中叫users表
    创建id 主键  自增
    创建字段username  长度为80的字符串  不允许为空   值唯一   加索引
    创建字段age   整数   允许为空
    创建字段email 长度为120的字符串  值唯一
"""


# class User(db.Model):
#     username = db.Column(db.String(80), unique=True)
#     pw_hash = db.Column(db.String(80))


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80),
                         nullable=False,
                         unique=True,
                         index=True)
    age = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(120), unique=True)
    # 增加一个字段 isActive,默认值为True
    isActive = db.Column(db.Boolean, default=True)


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sname = db.Column(db.String(30), nullable=False)
    sage = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)


class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer, primary_key=True)
    tname = db.Column(db.String(30), nullable=False)
    tage = db.Column(db.Integer, nullable=False)
    cid = db.Column(db.Integer, db.ForeignKey('course.id'))


class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(30), nullable=False, unique=True)
    # 增加反向引用关系属性：针对Teacher类
    # 关联属性：course_teachers
    # 反向引用关联属性：teacher_course
    course_teachers = db.relationship(
        'Teacher',
        backref='teacher_course',
        lazy='dynamic'
    )


# db.drop_all()  # 删除所有的表结构,重新构建新的表结构
# db.drop_all()
# db.create_all()


@app.route('/00-page')
def page():
    return render_template('00-page.html')


@app.route('/01-request')
def request_views():
    # print(request.scheme)
    # print(request.method)
    # print(request.args)
    # print(request.form)
    # print(request.cookies)
    # print(request.url)
    # print(request.path)
    # print(request.full_path)
    # print(request.headers)
    # 判断Referer 在request.headers 中是否存在
    if 'Referer' in request.headers:
        print('Referer:', request.headers['Referer'])
    url = request.headers.get(key='Referer', default='/')  # request结构： 字典.get()  若Referer有值，则取其值，否则取‘/’
    print('返回到：', url)
    return 'a'


@app.route('/02-page')
def page02():
    return render_template('02-page.html')


@app.route('/02-get')
def get_views():
    # 接收前端传过来的kw的值
    kw = request.args.get(key='kw', default='暂无')
    return '传递过来的参数值为：' + kw


@app.route('/03-page')
def page03():
    return render_template('03-page.html')


@app.route('/03-post', methods=["get", "post"])
def post_views():
    uname = request.form['uname']
    upwd = request.form['upwd']
    return "用户名称：%s, 用户密码：%s" % (uname, upwd)


@app.route('/04-login', methods=['get', "post"])
def login():
    # 通过request.method来判断用户的请求方式
    if request.method == 'GET':
        return render_template('04-login.html')
    uname = request.form['uname']
    upwd = request.form['upwd']
    return "用户名称：%s, 用户密码：%s" % (uname, upwd)


@app.route('/01-file', methods=['get', 'post'])
def file_views():
    if request.method == 'GET':
        return render_template('01-file.html')
    uname = request.form['uname']
    if request.files:
        f = request.files['uimg']
        # f.save('static/' + f.filename)
        # f.save('static/%s.png' % uname)
        filename = uname + util.generate_time() + '.' + util.file_strtype(f)
        """
         # 使用时间作为文件名 保证文件名不重复   文件路径为相对路径
        f.save('static/%s'
               % filename)
        """
        # 文件路径是绝对路径
        basedir = os.path.dirname(__file__)
        upload_path = os.path.join(basedir, 'static', filename)
        f.save(upload_path)
    return '数据处理成功！'


@app.route('/03-add')
def add_views():
    # 创建实体类对象
    user = Users()
    user.username = 'hdm'
    user.age = 26
    user.email = 'hdm@163.com'
    # 保存实体对象回数据库
    db.session.add(user)
    # db.session.commit()   # 非查询   app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']= True
    return "增加数据成功"


@app.route('/04-register', methods=['get', 'post'])
def register_views():
    if request.method == 'GET':
        return render_template('04-register.html')
    user = Users()
    username = request.form['uname']
    age = request.form['uage']
    email = request.form['uemail']
    user.username = username
    user.age = age
    user.email = email
    db.session.add(user)
    return '注册成功'


@app.route('/05-query')
def query_views():
    query = db.session.query(Users)
    # print(query)
    # # SELECT users.id AS users_id, users.username AS users_username, users.age AS users_age, users.email AS users_email FROM users
    # print('type:',type(query))
    # print(query.all())   # [<Users 1>, <Users 6>, <Users 8>, <Users 9>]
    # print(query.first().id)
    # print(query.count())
    users = query.all()
    for user in users:
        print('id:%s,姓名：%s,年龄：%s' % (user.id, user.username, user.age))
    print("user表中共有%d条数据。" % query.count())
    return "查询成功"


@app.route('/06-filter')
def filter_views():
    #  and -->  ,
    # users = db.session.query(Users).filter(
    #     Users.age < 30,
    #     Users.id>1
    # ).all()
    # or  -->  or_()
    users = db.session.query(Users).filter(
        or_(
            Users.age < 30,
            Users.id > 1
        )
    ).all()
    print(users)
    for user in users:
        print('id:%s,姓名：%s,年龄：%s' % (user.id, user.username, user.age))
    return "执行查询成功"


@app.route('/09-orderby')
def orderby_views():
    users = db.session.query(Users).order_by(Users.age.desc(), Users.id).filter(Users.age > 18).all()
    # users = db.session.query(Users).order_by('age desc,id').filter(Users.age>18).all()   #  版本问题
    for user in users:
        print('id:%s,姓名：%s,年龄：%s' % (user.id, user.username, user.age))
    return "执行查询成功"


@app.route('/10-Aggregate')
def Aggregate_views():
    values = db.session.query(
        func.sum(Users.age),
        func.avg(Users.age),
        func.max(Users.age),
        func.min(Users.age)
    ).filter(Users.age > 25).all()
    # print(values)
    # print(type(values))
    for value in values:
        print("年龄的和是：%s" % value[0])
        print("年龄的平均值是：%s" % value[1])
        print("最大年龄是：%s" % value[2])
        print("最小年龄是：%s" % value[3])
    # Users实体中，按isActive分组，每组的人数
    res = db.session.query(
        Users.isActive,
        func.count(Users.id)
    ).group_by('isActive').all()
    print(res)

    # 按isActive分组后，组内人数大于1人的组名和人数  且年龄大于25
    re = db.session.query(
        Users.isActive,
        func.count(Users.id)
    ).filter(Users.age > 25) \
        .group_by('isActive') \
        .having(func.count(Users.id) > 1).all()
    print(re)
    return "聚合查询成功"


@app.route('/11-groupby')
def groupby_views():
    """
        1、查询users表中所有人的总年龄
        2、查询users表中总人数是多少
        3、查询users表中年龄大于25的人的平均年龄
        4、查询users表中按isActive分组后每组的人数
    """
    re01 = db.session.query(
        func.sum(Users.age)
    ).all()
    print("所有人的总年龄：%s" % re01)
    re02 = db.session.query(
        func.count(Users.id)
    ).all()
    print("总人数是：%s" % re02)
    re03 = db.session.query(
        func.avg(Users.age)
    ).filter(Users.age > 25).all()
    print("年龄大于25的人的平均年龄是：%s" % re03)
    re04 = db.session.query(
        func.count(Users.id)
    ).group_by('isActive').all()
    print("按isActive分组后每组的人数是：%s" % re04)
    return "聚合查询成功"


@app.route('/12-update')
def update_views():
    # 修改id为6的username和isActive的值
    # 查
    user = Users.query.filter_by(id=6).first()
    # 改
    user.username = 'meimei'
    user.isActive = False
    # 保存
    db.session.add(user)
    return redirect('/05-query')


@app.route('/13-regteacher')
def refteacher_views():
    """
    # 方案1：声明一个teacher对象并赋值，同时指定cid的值来关联对应的课程
    teacher = Teacher()
    teacher.tname = '魏老师'
    teacher.tage = 35
    teacher.cid = 1
    db.session.add(teacher)
    """
    # 方案2：声明一个teacher对象并赋值，通过teacher_course属性来关联对应的Course信息
    # 通过 teacher.teacher_course 得到关联的course对象

    # 查询出id=2的course的信息
    cour = Course.query.filter_by(id=2).first()
    tea = Teacher()
    tea.tname = "王老师"
    tea.tage = 33
    tea.teacher_course = cour
    db.session.add(tea)
    return "增加老师成功！"


@app.route('/14-regtea', methods=['GET', 'POST'])
def regtea_views():
    if request.method == 'GET':
        return render_template('14-regtea.html')
    # cname = int(request.form['cname'])
    cname = request.form['id']
    tname = request.form['tname']
    tage = request.form['tage']
    cour = Course.query.filter_by(id=cname).first()
    tea = Teacher()
    tea.tname = tname
    # tea.tage = int(tage)
    tea.tage = tage
    # print(tea.tname,tea.tage)
    tea.teacher_course = cour
    db.session.add(tea)
    return redirect('/14-regtea')   #  跳转   重定向


if __name__ == '__main__':
    # app.run(debug=True)
    manager.run()
