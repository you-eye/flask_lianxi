import datetime

from ext import db


class Goods(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Float, nullable=False)
    pwd = db.Column(db.String(256), nullable=False)
    pdate = db.Column(db.DateTime, default=datetime.datetime.now)
