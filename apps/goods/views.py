from flask import Blueprint

goods_bp = Blueprint('goods', __name__)


@goods_bp.route('/goods/')
def goods_index():
    return 'youdiangaoahahaha'
