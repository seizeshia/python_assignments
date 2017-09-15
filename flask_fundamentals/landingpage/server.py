
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def dojo():
        return render_template('dojo.html')
        name = request.form['name']
@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')
@app.route('/dojo', methods=['POST'])
def index():
    return render_template('index.html')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

app.run(debug=True)
