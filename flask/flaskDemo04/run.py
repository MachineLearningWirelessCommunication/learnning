from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate

shopApp = Flask(__name__)

# 连接数据库
shopApp.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456' \
                                            '@172.27.28.50:3306/shops'
# 指定信号追踪
shopApp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 配置自动提交操作回数据库
shopApp.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(shopApp)
print(db)


# 创建Manager 实例  并指定要管理哪个app
manager = Manager(shopApp)
# 创建Migrate 对象   并指定要关联的app和db
migrate = Migrate(shopApp,db)
# 为manager 增加数据迁移的子命令
manager.add_command('db',MigrateCommand)


# 创建数据表
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(20), nullable=False,unique=True)
    password = db.Column(db.String(12), nullable=False)


@shopApp.route('/login', methods=['GET', 'POST'])
def login_views():
    if request.method == 'GET':
        return render_template('login.html')
    user_name = request.form['uname']
    pwd = request.form['upwd']
    user = db.session.query(Users).filter(Users.user_name == user_name).first()
    if not user:
        return "用户不存在！"
    elif user.password != pwd:
        return "密码不正确！"
    else:
        return redirect('/index')


@shopApp.route('/register', methods=['GET', 'POST'])
def register_views():
    if request.method == 'GET':
        return render_template('register.html')
    user_name = request.form['uname']
    pwd = request.form['upwd']
    repwd = request.form['urepwd']
    if db.session.query(Users).filter(Users.user_name == user_name).first():
        return "该用户已存在！"
    if pwd != repwd or not pwd:
        return redirect('/register')
    user = Users()
    user.user_name = user_name
    user.password = pwd
    db.session.add(user)
    return redirect('/login')


@shopApp.route('/index')
def index_views():
    return render_template('index.html')



if __name__ == '__main__':
    # shopApp.run(debug=True)
    manager.run()