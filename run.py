from app import creat_app
from flask_cors import CORS
from config import configer
import app.admin.views as admin_views

environment = configer.get('environment', 'name')
HOST = configer.get('service', 'ip')
PORT = configer.get('service', 'port')

app = creat_app(environment)
CORS(app)

# admin相关
app.add_url_rule('/index', view_func=admin_views.index, methods=['GET'])
app.add_url_rule('/admin/auth/user/add', view_func=admin_views.add_user, methods=['POST'])  # 增加用户
app.add_url_rule('/admin/auth/user/view', view_func=admin_views.get_users, methods=['GET'])  # 查看全部用户信息
app.add_url_rule('/admin/auth/user/delete/<name>', view_func=admin_views.delete_user, methods=['DELETE'])  # 删除用户
app.add_url_rule('/admin/auth/user/change', view_func=admin_views.change_user, methods=['POST'])  # 修改用户信息


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=app.config.get('DEBUG'))
