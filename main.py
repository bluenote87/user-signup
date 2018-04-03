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
    elif un.length < 3 or un.length > 20:
        un_error = "That's not a valid username"

    un_ver = re.match(r'\s\W', un)
    if un_ver:
        un_error = "That's not a valid username"

    if pw == "":
        pw_error = "That's not a valid password"
    elif pw.length < 3 or pw.length > 20:
        pw_error = "That's not a valid password"
    
    pw_ver = re.match(r'\s', pw)
    if pw_ver:
        pw_error = "That's not a valid password"

    if pv == "":
        pv_error = "Passwords don't match"
    elif pv.length < 3 or pv.length > 20:
        pv_error = "Passwords don't match"
    elif pv != pw:
        pv_error = "Passwords don't match"

    em_ver = re.match(r'@{1}\.+', em)
    em_space = re.match(r'\s', em)
        if em_space or not em_ver:
            em_error = "That's not a valid email"

    if un_error or pw_error or pv_error or em_error:
        return render_template('index.html', un_error = un_error, pw_error = pw_error,
        pv_error = pv_error, em_error = em_error)
    else:
        return redirect('/welcome?username={0}'.format(un))



@app.route("/welcome", methods = ['GET']):
def welcome():
    name = request.args.get('username')
    return render_template('welcome.html', name = name)

app.run()