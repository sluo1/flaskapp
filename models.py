__author__ = 'tommy'
from __init__ import db

class User(db.Model):
    #__tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(320))
    password = db.Column(db.String(32), nullable=False)
    memos = db.relationship('Memo',backref='author',lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % self.username


class Memo(db.Model):
    #__tablename__= 'memo'
    id = db.Column(db.Integer,primary_key=True)
    event=db.Column(db.String(200))
    update_time=db.Column(db.DateTime)
    create_time=db.Column(db.DateTime)
    username=db.Column(db.String(80),db.ForeignKey('user.username'))

    def __repr__(self):
        return '<Memo %r>' %(self.event)

