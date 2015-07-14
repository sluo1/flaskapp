from __init__ import db
import models
from models import User,Memo
# db.create_all()
# users=models.User.query.all()
# for user in users:
#     db.session.delete(user)
# db.session.commit()
#
# db.drop_all()
# db.create_all()
#
# events=models.Memo.query.all()
# for event in events:
#     db.session.delete(event)
#
# db.session.commit()

db.drop_all()
db.create_all()