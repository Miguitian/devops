import pathlib
import sys
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
_project_root = str(pathlib.Path(__file__).resolve().parents[1])
sys.path.append(_project_root)
from config import config

moment = Moment()
bootstrap = Bootstrap()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def creat_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    moment.init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    # from .admin import admin as main_blueprint   # 这里需要注册蓝图
    # app.register_blueprint(main_blueprint, url_prefix='/admin/') 暂不使用蓝图功能
    return app
