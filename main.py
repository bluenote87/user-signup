from flask import Flask, request, redirect, render_template
import os
import cgi
import re


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/"):
def index():
    return render_template('index.html')
    
@app.route("/", methods = ['POST']):
def index():
    un = request.form['username']
    pw = request.form['password']
    pv = request.form['verify']
    em = request.form['email']

    un_error = ""
    pw_error = ""
    pv_error = ""
    em_error = ""

    if un == "":
        un_error = "That's not a valid username"
    elif un.length <= 2:
        un_error = "That's not a valid username"

    if pw == "":
        pw_error = "That's not a valid password"
    elif pw.length <= 2:
        pw_error = "That's not a valid password"

    if pv == "":
        pv_error = "Passwords don't match"
    elif pv.length <= 2:
        pv_error = "Passwords don't match"
    elif pv != pw:
        pv_error = "Passwords don't match"

    return render_template('index.html')



@app.route("/welcome", methods = ['GET']):
def welcome():
    name = request.args.get('username')
    return render_template('welcome.html', name = name)

app.run()