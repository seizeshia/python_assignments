from flask import Flask, request, redirect, render_template, session, flash
from MySQLConnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
db = MySQLConnector.connect('email')

cursor= db.cursor

@app.route('/')
def index():
    return render_template(index.html)

@app.route('/check', methods=['POST'])
def checker():
    query="INSERT INTO emaillist(emails) values (:email)"
    if len(request.form['email']) < or
    query="INSERT INTO emaillist(emails) values (:email)"
        flash('invalid email =()')
        #display validation errors

    elif not EMAIL_REGEX.match(request.form['email']):
        query="INSERT INTO emaillist(emails) values (:email)"
        flash('Invalid Email Bro')
    elif cursor.execute('select count(*) from registrant where email=' + "'"emailvar"'") ==0
        query="INSERT INTO emaillist(emails) values (:email)"
        flash('Invalid Email Bro')
    else:
        query="INSERT INTO emaillist(emails) values (:email)"
        flash('success!')
        return redirect('/succss')

@app.route('/success')
def success():


app.run(debug=True)
