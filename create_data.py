from __init__ import db
import models
from models import User,Memo
import datetime

u1=User(username='tommy',email='tommy@zamplus.com',password='123456')
db.session.add(u1)
db.session.commit()

u2=User(username='3434522',email='3434522@qq.com',password='123456')
db.session.add(u2)
db.session.commit()

u3=User(username='37371759',email='37371759@qq.com',password='123456')
db.session.add(u3)
db.session.commit()


m1=Memo(event='eat food',update_time=datetime.datetime.utcnow(),create_time=datetime.datetime.utcnow(),author=u1)
db.session.add(m1)
db.session.commit()

m2=Memo(event='drink water',update_time=datetime.datetime.utcnow(),create_time=datetime.datetime.utcnow(),author=u1)
db.session.add(m2)
db.session.commit()

m3=Memo(event='play football',update_time=datetime.datetime.utcnow(),create_time=datetime.datetime.utcnow(),author=u2)
db.session.add(m3)
db.session.commit()

m4=Memo(event='watch tv',update_time=datetime.datetime.utcnow(),create_time=datetime.datetime.utcnow(),author=u3)
db.session.add(m4)
db.session.commit()