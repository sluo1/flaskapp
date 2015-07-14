from wtforms import Form,PasswordField,validators
from wtforms import StringField,BooleanField,TextAreaField,TextField
from wtforms.validators import DataRequired,Length,Required


class AddForm(Form):
    username=StringField('username',[validators.Length(min=0, max=100)])
    email=StringField('email',[validators.Length(min=0, max=100)])
    password=StringField('password',[validators.Length(min=0, max=100)])

class EditForm(Form):
    username=StringField('username',[validators.Length(min=0, max=100)])
    email=StringField('email',[validators.Length(min=0, max=100)])
    password=StringField('password',[validators.Length(min=0, max=100)])
