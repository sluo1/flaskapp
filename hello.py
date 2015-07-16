import os
from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import abort,redirect,url_for

UPLOAD_FOLDER='/path/to/the/uploads'
ALLOWED_EXTENSIONS=set(['txt','pdf','png','jpg','jpeg','gif'])

app=Flask(__name__)
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

@app.route("/")
def index():
    #return "index page"
    return redirect(url_for('logintest'))
@app.route("/logintest")
def logintest():
    return "this is login page"

@app.route("/setcookie")

def setcookie():
    resp=make_response(render_template('hello.html'))
    resp.set_cookie('username','the username')
    return resp

@app.route("/getcookie")
def getcookie():
    username=request.cookies.get('username')
    return username


@app.route('/user/<username>')
def show_username(username):
    return "username: %s" %username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return "postid: %d" %post_id

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=='POST':
        do_the_login()
    else:
        show_the_login_form()

def do_the_login():
    pass

def show_the_login_form():
    pass

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template('hello.html',name=name)


if __name__=="__main__":
    app.debug=True
    app.run('0.0.0.0')
