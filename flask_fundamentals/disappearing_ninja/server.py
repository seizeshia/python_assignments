from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>No ninjas here!</h1>'


@app.route('/ninja')
def ninja():
    return render_template('index.html')

@app.route('/ninja/<color>')
def ninjas(color):
    if color == 'red':
        change = '/static/raphael.jpg'
    elif color == 'blue':
        change = '/static/leonardo.jpg'
    elif color == 'orange':
        change = '/static/michelangelo.jpg'
    elif color == 'purple':
        change = '/static/donatello.jpg'
    else:
        change = '/static/april.jpg'
    return render_template('individualninja.html', change=change)

app.run(debug=True)
