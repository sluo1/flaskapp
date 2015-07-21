__author__ = 'tommy'
from __init__ import app,db
from flask import render_template,flash,redirect,session,url_for,request,g,abort
import models
from forms import AddUserForm,AddMemoForm
from models import User,Memo
import datetime
from flask.ext.login import login_user,logout_user,login_required
from selflib import get_md5

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
    u=models.User.query.first()
    form=AddMemoForm(request.form)
    if request.method=='POST':
        m=Memo(event=form.event.data,create_time=datetime.datetime.utcnow(),doevent_day=form.doevent_day.data,author=u)
        print m
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


@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template("login.html")
    elif request.method=='POST':
        # print "ccc"
        # print request.form['username']
        # print get_md5(request.form['password'])
        # suser=User.query.filter_by(username=request.form['username'],password=get_md5(request.form['password'])).first()
        # print 'aaa'
        form_dict=dict(request.form)
        s_user = User.query.filter_by(username=form_dict['name'][0],\
                password=get_md5(form_dict['password'][0])).first()
        if s_user:
            g.user=s_user
            print 'bbb'
            flash('login success','success')
            return redirect(url_for('user'))
        else:
            flash('user or password wrong,please try again','fail')
            return redirect(url_for('login'))
    else:
        abort(404)





