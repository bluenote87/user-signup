from flask import Flask, request, redirect, render_template
import cgi
import re


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')
    
@app.route("/", methods = ['POST'])
def validate():
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
    elif len(un) < 3 or len(un) > 20:
        un_error = "That's not a valid username"

    un_ver = re.search(r'\s|\W', un)
    if un_ver:
        un_error = "That's not a valid username"

    if pw == "":
        pw_error = "That's not a valid password"
    elif len(pw) < 3 or len(pw) > 20:
        pw_error = "That's not a valid password"
    
    pw_ver = re.search(r'\s', pw)
    if pw_ver:
        pw_error = "That's not a valid password"

    if pv == "":
        pv_error = "Passwords don't match"
    elif len(pv) < 3 or len(pv) > 20:
        pv_error = "Passwords don't match"
    elif pv != pw:
        pv_error = "Passwords don't match"

    if em:
        em_ver = re.search(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', em, re.I)
        if not em_ver:
            em_error = "That's not a valid email"

    if un_error or pw_error or pv_error or em_error:
        return render_template('index.html', un_error = un_error, pw_error = pw_error,
        pv_error = pv_error, em_error = em_error, username = un, email = em)
    else:
        return redirect('/welcome?username={0}'.format(un))



@app.route("/welcome", methods = ['GET'])
def welcome():
    name = request.args.get('username')
    return render_template('welcome.html', name = name)

app.run()