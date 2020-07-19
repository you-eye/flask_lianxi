from flask import Blueprint

order_bp = Blueprint('order', __name__)


@order_bp.route('/order/')
def index():
    return "orderceshi"
