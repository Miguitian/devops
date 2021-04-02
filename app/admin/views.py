import traceback
import sys

try:
    from __init__ import _project_root

    sys.path.append(_project_root)
except Exception as e:
    traceback.print_exc()
from flask import jsonify, request
from app.Database import models, database
from logger import logger
from app.Basic import schemas


def index():
    return "YES! ok"


def add_user():
    """
    管理员增加用户
    保证用户名称唯一

    name: 用户名称
    password: 用户密码
    info: 用户信息
    roles: 用户角色

    Returns:
        返回创建时的信息（成功、失败、重复）

    """
    res = request.json
    if not res:
        return jsonify({"Code": 400, "Message": "Not in json format"}), 400
    name = res["name"]
    password = res["password"]
    info = res.get('info', '')
    roles = res.get('roles', schemas.RolesEnum.USER)  # 默认一个角色，这里需要设置schema
    obj = schemas.AddUser(
        name=name,
        password=password,
        info=info,
        roles=roles
    )
    __status = database.AddUser(obj)
    if __status:
        return jsonify({"Code": 200, "Message": '添加成功'}), 200
    else:
        return jsonify({"Code": 400, "Message": '添加失败'}), 400


def delete_user(name: str):
    """
    通过用户名删除一个用户
    Args:
        name: 用户名称

    Returns:
        success、failure

    """
    pass


def get_users() -> list:
    """
    获取用户列表
    [{}]
    Returns:
    """
    try:
        __user_list = database.GetUsers()
        users = {"users": __user_list}
        return jsonify(users), 200
    except Exception:
        traceback.print_exc()
        return jsonify({"Code": 400, "Message": '查询用户列表失败'}), 400


def change_user():
    """
    通过传入参数，修改用户信息
    必须包含以下字段，且以下字段不能修改
    name: 用户名称

    Returns:

    """
    pass
