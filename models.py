__author__ = 'tommy'
from __init__ import db
from selflib import get_md5

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(320))
    password = db.Column(db.String(32), nullable=False)
    memos = db.relationship('Memo',backref='author',lazy='dynamic')

    def __init__(self,username,email,password):
        self.username=username
        self.email=email
        self.password=get_md5(password)

    def __repr__(self):
        return '<User %r>' % self.username


class Memo(db.Model):
    __tablename__= 'memo'
    id = db.Column(db.Integer,primary_key=True)
    event=db.Column(db.String(200))
    doevent_day=db.Column(db.String(50))
    create_time=db.Column(db.DateTime)
    user_name = db.Column(db.String(50), db.ForeignKey('user.username'))

    def __repr__(self):
        return '<Memo %r>' %(self.event)


