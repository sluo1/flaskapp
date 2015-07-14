from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)
#app.config.from_object('config')
db=SQLAlchemy(app)
app.config['SECRET_KEY']='you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/test?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

import views,models

