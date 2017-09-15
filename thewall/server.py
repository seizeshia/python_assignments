from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app,'walldb')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app.secret_key = "ThisisSecret"

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/logincheck', methods=["post"])
def logincheck():
    # wallDB = mysql.query_db('SELECT email, password FROM users')
    query = "SELECT email, password from users WHERE email=:email AND password=:password;"
    data = {'email': request.form['emaillog'], 'password': request.form['passwordlog']}
    loginresult = mysql.query_db(query, data)
    if len(loginresult)>0:
        findname= "SELECT first_name from users where email=:email;"
        info={'email': request.form['emaillog'], 'first_name':'first_name'}
        # for first_name in users:
        #     where
        x = mysql.query_db(findname,info)[0]

        session['name'] = x['first_name']
        return redirect('/wall')

    else:
        flash("wrong email or password")

    # if mysql.query_db(query, data) != []
    #     flash("wrong email or password")
    # else:
    return redirect('/')

@app.route('/regcheck', methods=['POST'])
def regcheck():
    query= "SELECT email FROM users where email=:email"
    data = {'email': request.form['emailreg']}
    registerresult= mysql.query_db(query, data)
    if len(registerresult) > 0:
        flash('Email is already registered!  Please log in!')
        if len(request.form['emailreg']) < 2:
            flash('Invalid email')
            if not EMAIL_REGEX.match(request.form['emailreg']):
                flash('Invalid Email!')
                if len(registerresult) == 0 and len(request.form[password]>5):
                    assign="INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, now(), now())"
                    data = {
                    'first_name': request.form['first_name'],
                    'last_name': request.form['last_name'],
                    'email': request.form['emailreg'],
                    'password': request.form['passwordreg']
                    }
                    session['first.name']=request.form['first_name']
                    sesssion['last.name']=request.form['last_name']
                    return redirect('/wall',)
                else:
                    flash("email or password error")
    return redirect('/')


@app.route('/wall')
def wall():
    displayer= "SELECT * FROM messages "
    messagess = mysql.query_db(displayer)
    return render_template('wall.html', messagess=messagess)

@app.route('/messagesubmit', methods=["POST"])
def messagesubmit():
    messagesubmit="INSERT INTO messages (message, created_at, updated_at) VALUES (:message, now(), now())"
    data = {
    'message': request.form['message']
    }
    mysql.query_db(messagesubmit, data)
    return redirect('/wall')

app.run(debug=True)
