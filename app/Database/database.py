#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    desc: 用于操作数据库
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
from app.Database.models import db_session
from app.Database import models
from app.Basic import schemas


def AddUser(obj) -> bool:
    """
    增加用户
    Args:
        obj: 创建用户的对象

    Returns:
        True/False

    """
    try:
        data = models.User(
            name=obj.name, password=obj.password, info=obj.info, roles=obj.roles
        )
        db_session.add(data)
        db_session.commit()
        return True
    except Exception:
        traceback.print_exc()
        return False


def GetUsers() -> list:
    """
    查询所有用户的信息
    Returns:
        返回查询到的所有用户信息

    """
    __users_list = []
    results = db_session.query(models.User.name, models.User.info, models.User.roles).all()
    for result in results:
        user = models.schemas.GetUserInfo(
                    name=result[0],
                    result=result[1],
                    roles=result[2]
                )
        __users_list.append(user.__dict__)
    return __users_list


if __name__ == '__main__':
    GetUsers()
