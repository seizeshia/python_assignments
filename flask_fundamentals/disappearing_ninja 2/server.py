from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ninja', methods=['get'])
def ninja():
    render_template('static/tmnt.png')

@app.route('/ninjas/<color>')
def ninjas(color):
    if color =='red':
        changes = '/static/raphael.jpg'
    elif color == 'blue':
        changes = '/static/leonardo.jpg'
    elif color == 'orange':
        changes = '/static/michelangelo.jpg'
    elif color == 'purple':
        changes = '/static/donatello.jpg'
    return render_template('individualninja.html', ninja = ninja, displayall=displayall)

app.run(debug=True)
