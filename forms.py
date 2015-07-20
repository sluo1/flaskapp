from wtforms import Form,PasswordField,validators
from wtforms import StringField,BooleanField,TextAreaField,TextField
from wtforms.validators import DataRequired,Length,Required
from datetime import datetime

class AddUserForm(Form):
    username=StringField('username',[validators.Length(min=0, max=100)])
    email=StringField('email',[validators.Length(min=0, max=100)])
    password=StringField('password',[validators.Length(min=0, max=100)])


class AddMemoForm(Form):
    #username=StringField('username',[validators.Length(min=0,max=100)])
    event=TextAreaField('event',[validators.Length(min=0,max=300)])
    create_time=datetime.utcnow()
    update_time=datetime.utcnow()