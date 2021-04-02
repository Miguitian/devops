import pathlib
import sys
import os
from configparser import ConfigParser

_project_root = str(pathlib.Path(__file__).resolve().parents[0])
sys.path.append(_project_root)

configer = ConfigParser()
configer.read(os.path.join(_project_root, 'config.ini'), encoding='utf-8')


class Config(object):
    JSON_AS_ASCII = False  # 避免jsonify 出现中文乱码
    DEBUG = True
    DIALECT = configer.get('database', 'dialect')
    DRIVER = configer.get('database', 'driver')
    CHARSET = configer.get('database', 'charset')
    POOL_SIZE = int(configer.get('database', 'pool_size'))
    ECHO = configer.get('database', 'echo')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_POOL_SIZE = POOL_SIZE
    SQLALCHEMY_ECHO = ECHO
    LOG_PATH = configer.get('log', 'log_path')
    LOG_LEVEL = configer.get('log', 'log_level')


class TestConfig(Config):
    DEBUG = True
    DATABASE_NAME = ''
    USER = ''
    PASSWORD = ''
    HOST = ''
    PORT = ''
    SQLALCHEMY_DATABASE_URI = '{dialect}+{driver}://{user}:{password}@{host}:{port}/{db_name}'.format(
        dialect=Config.DIALECT, driver=Config.DRIVER, user=USER, password=PASSWORD, host=HOST, port=PORT,
        db_name=DATABASE_NAME)


class DevelopConfig(Config):
    DEBUG = True
    DATABASE_NAME = 'devops'
    USER = 'root'
    PASSWORD = 123456
    HOST = '127.0.0.1'
    PORT = 3306
    SQLALCHEMY_DATABASE_URI = '{dialect}+{driver}://{user}:{password}@{host}:{port}/{db_name}'.format(
        dialect=Config.DIALECT, driver=Config.DRIVER, user=USER, password=PASSWORD, host=HOST, port=PORT,
        db_name=DATABASE_NAME)


class ProductionConfig(Config):
    DATABASE_NAME = configer.get('database', 'database_name')
    USER = configer.get('database', 'user')
    PASSWORD = configer.get('database', 'password')
    HOST = configer.get('database', 'host')
    PORT = configer.get('database', 'port')
    SQLALCHEMY_DATABASE_URI = '{dialect}+{driver}://{user}:{password}@{host}:{port}/{db_name}'.format(
        dialect=Config.DIALECT, driver=Config.DRIVER, user=USER, password=PASSWORD, host=HOST, port=PORT,
        db_name=DATABASE_NAME)


config = {
    'develop': DevelopConfig,
    'test': TestConfig,
    'product': ProductionConfig,
    configer.get('environment', 'name'): ProductionConfig
}

config_manager = config[configer.get('environment', 'name')]
