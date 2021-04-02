import traceback
import sys

try:
    from __init__ import _project_root

    sys.path.append(_project_root)
except Exception as e:
    traceback.print_exc()
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from config import config_manager
from app.Basic import schemas

engine = create_engine(config_manager.SQLALCHEMY_DATABASE_URI, echo=int(config_manager.ECHO),
                       convert_unicode=True, encoding='utf8',
                       pool_size=config_manager.SQLALCHEMY_POOL_SIZE)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=True, bind=engine))
Base = declarative_base()


class User(Base, UserMixin):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(50), unique=True)  # unique 唯一性
    password_hash = Column('password_hash', String(128), nullable=False)
    roles = Column('roles', String(64), default=schemas.RolesEnum.USER)
    info = Column('info', String(128), default='')

    def __str__(self):
        return self.name + ' ' + str(self.id)

    @property
    def password(self):
        raise AttributeError('密码不可读取')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


from app import login_manager
@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=int(id))


def init_db():
    """
    初始化数据库
    Returns:

    """
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
