from flask import Flask

import settings
from apps.goods.views import goods_bp
from apps.user.view import user_bp
from ext import db


def create_app():
    app = Flask(__name__, template_folder='../templates')
    app.config.from_object(settings.DevelopmentConfig)
    # 将db与app进行关联
    db.init_app(app)
    # 注册蓝图
    app.register_blueprint(user_bp)

    app.register_blueprint(goods_bp)

    return app
