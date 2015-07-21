from wtforms import Form,PasswordField,validators
from wtforms import StringField,BooleanField,TextAreaField,TextField,PasswordField
from wtforms.validators import DataRequired,Length,Required
from datetime import datetime
from flask import g
from flask.ext.login import login_user,logout_user,current_user,login_required

class AddUserForm(Form):
    username=StringField('username',[validators.Length(min=0, max=100)])
    email=StringField('email',[validators.Length(min=0, max=100)])
    password=PasswordField('password',[validators.Length(min=0, max=100)])


class AddMemoForm(Form):
    #username=StringField('username',[validators.Length(min=0,max=100)])
    event=TextAreaField('event',[validators.Length(min=0,max=300)])
    doevent_day=StringField('doevent_day',[validators.Length(min=0,max=100)])
    create_time=datetime.utcnow()
