#encoding=utf-8
import os
from flask import Flask

def create_app(test_config=None):
    # 创建和配置app
    app = Flask(__name__,instance_relative_config=True) #创建flask实例
    #secret_key和database默认配置项，mapping用于默认配置
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path,'flaskr.sqlite'),
    )
    #确认测试的配置文件是否存在
    if test_config is None:
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello World!'
    #导入db
    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/',endpoint='index')

    return app