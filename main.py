from flask import Flask, request
import os
import re


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods = ['POST', 'GET']):
def index():


app.run()