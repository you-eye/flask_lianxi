from datetime import datetime

from ext import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(24), unique=True)
    rdatetime = db.Column(db.DateTime, default=datetime.now)

    def __str__(self):
        return self.username


class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    realname = db.Column(db.String(24))
    gender = db.Column(db.Boolean, default=False)
