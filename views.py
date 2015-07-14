__author__ = 'tommy'
from __init__ import app,db
from flask import render_template,flash,redirect,session,url_for,request,g
import models
from forms import AddForm,EditForm
from models import User,Memo


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user')
def user():
    users=models.User.query.all()
    return render_template('user.html',users=users)

@app.route('/memo')
def memo():
    events=models.Memo.query.all()
    return render_template('memo.html',events=events)

@app.route('/add',methods=['GET','POST'])
def add():
    form=AddForm(request.form)
    #users=models.User.query.all()
    if request.method == 'POST' and form.validate():
        u=User(username=form.username.data,email=form.email.data,password=form.password.data)
        db.session.add(u)
        db.session.commit()
        flash("your changes have been saved.")
        return redirect(url_for('user'))

    return render_template('add.html',form=form)


@app.route("/testform")
def testform():
    return render_template('testform.html')


# @app.route('/edituser',methods=['GET','POST'])
# def edituser():
#     username=models.User.username

