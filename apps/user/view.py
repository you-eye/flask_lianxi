from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import or_

from apps.user.model import User
from ext import db

user_bp = Blueprint('user', __name__)


@user_bp.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':

        return render_template('register.html')
    else:
        print(request.form)
        print(dict(request.form))
        username = request.form.get('username')
        paw = request.form.get('password')
        rpaw = request.form.get('repassword')
        phone = request.form.get('phone')
        if username:
            print('aaaa')
        if paw:
            print('bbb')
        if paw == rpaw:
            user = User()
            user.username = username
            user.password = paw
            user.phone = phone
            db.session.add(user)
            db.session.commit()
            # user.save()
            return redirect(url_for('user.index'))
        else:
            return '密码不一致'


@user_bp.route('/index1/')
def index():
    # 查询数据库中的数据
    users = User.query.all()
    # print(users)
    return render_template('user_center.html', users=users)


@user_bp.route('/search')
def search():
    keyword = request.args.get('search')
    password = request.args.get('password')
    print(keyword)
    # 查询
    user_list = User.query.filter(or_(User.username.contains(keyword), User.phone.contains(keyword))).all()
    return render_template('user_center.html', users=user_list)


@user_bp.route('/delete')
def delete():
    uid = request.args.get('uid')
    user = User.query.get(uid)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('user.index'))
