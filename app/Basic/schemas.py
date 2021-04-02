# -*- coding: utf-8 -*-
"""
    desc: 本项目涉及的所有的实体模型
    author: miguitian
    date: 2021-03-31
"""
import traceback
import sys
try:
    from __init__ import _project_root
    sys.path.append(_project_root)
except Exception as e:
    traceback.print_exc()
from pydantic import BaseModel

class RolesEnum:
    ADMIN = "admin"
    USER = "user"

class ABSBaseModel(BaseModel):
    """
    所有数据处理的基类
    """
    pass

class GetUserInfo(ABSBaseModel):
    """
    单个用户的所有信息
    """
    name: str
    info: str = ''
    roles: str

class AddUser(GetUserInfo):
    """
    创建用户时的信息
    """
    password: str


