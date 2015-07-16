__author__ = 'tommy'
from __init__ import app,db
from flask import render_template,flash,redirect,session,url_for,request,g
import models
from forms import AddUserForm,AddMemoForm
from models import User,Memo
from datetime import datetime


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

@app.route('/adduser',methods=['GET','POST'])
def adduser():
    form=AddUserForm(request.form)
    #users=models.User.query.all()
    if request.method == 'POST' and form.validate():
        u=User(username=request.form['username'],email=request.form['email'],password=form.password.data)
        db.session.add(u)
        db.session.commit()
        flash("user has been added.")
        return redirect(url_for('user'))

    return render_template('adduser.html',form=form)

@app.route('/addmemo',methods=['GET','POST'])
def addmemo():
    form=AddMemoForm(request.form)
    if request.method=='POST':

        m=Memo(username=models.User.query.first(),event=form.event.data,create_time=datetime.utcnow(),update_time=datetime.utcnow())
        db.session.add(m)
        db.session.commit()
        flash("your memo have been saved")
        return redirect(url_for('memo'))
    return render_template('addmemo.html',form=form)


@app.route("/testform",methods=['GET','POST'])
def testform():
    # if request.method=="POST":
    #     namevalue= request.form['name']
    #     passwordvalue= request.form['password']
    form=request.form
    return render_template('testform.html',form=form)




