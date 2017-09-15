from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app, 'newfriendsdb')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():

    return render_template('index.html')


@app.route('/regcheck', methods=["post"])
def registrationcheck():
    for email in users:
        if email == request.form['emailreg']:
            flash('Account already exists pleast log in')

    if len(reques.form['emailreg']) < 2:
        flash('invalid email')
    if not EMAIL_REGEX.match(request.form['emailreg']):
        flash('Invalid Email!')
    else:
        query="INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, now(), now())"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['emailreg'],
            'password': request.form['passwordreg']
            }
        mysql.query_db(query, data)
        return redirect('wall.html')


@app.route('/wall')
def wall():

    return render_template('wall.html')

# @app.route('/friends', methods=['POST'])
# def create():
#     query = "INSERT INTO friends (name, age, created_at, updated_at) Values (:name, :age, NOW(), NOW())"
#     data = {
#             'name': request.form['name'],
#             'age': request.form['age'],
#     }
#     mysql.query_db(query, data)
#     return redirect('/')


app.run(debug=True)
