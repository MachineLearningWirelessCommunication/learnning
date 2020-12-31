# flask框架练习，系统注册、登录


## 技术栈：
* flask框架的使用
* 数据库迁移


## 代码主体结构
from flask import Flask, render_template, request,redirect

from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager

from flask_migrate import MigrateCommand, Migrate


>创建应用
>>shopApp = Flask(__name__) 
>>>注： name  左右存在双下划线

>连接数据库
>>shopApp.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456' \
                                            '@172.27.28.50:3306/shops'
                                            
>指定信号追踪
>>shopApp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

>配置自动提交操作回数据库
>>shopApp.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(shopApp)
print(db)

>创建Manager 实例  并指定要管理哪个app
>>manager = Manager(shopApp)

>创建Migrate 对象   并指定要关联的app和db
>>migrate = Migrate(shopApp,db)

>为manager 增加数据迁移的子命令
>>manager.add_command('db',MigrateCommand)

>if __name__ == '__main__':
>>manager.run()

## 数据库迁移命令
> 初始化数据库
>>python xxx.py db init

>将编辑好的实体类生成一个中间文件并保存
>>python xxx.py db migrate

>将中间文件映射回数据库
>>python xxx.py db upgrade

## flask服务启动命令
>python xxx.py runserver