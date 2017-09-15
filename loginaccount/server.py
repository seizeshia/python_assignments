from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'logindeets')

@app.route('/')
def index():
    render_template(index.html)
@app.route('/')
def checker():
    for i in email
        if request.form['email'] == i['email']
            flash("email already exists!")
            <link src="www.apple.com">
        if len(request.form['email']) < 1:
            flash("you must enter an email!")
        if not EMAIL_REGEX.match(request.form['email']):
            flash("Invalid Email you filthy animal")
        else:
            if(len(request.form['first_name']) < 2):
                flash("Name is invalid")
            if isinstance(0,text)
