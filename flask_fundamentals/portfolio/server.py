
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
    def root():
        return render_template('index.html')

@app.ninjas('/ninjas'):
    def ninjas():
        return render_template('ninjas.html')
@app.dojo('/dojo', method=['POST']):
    def dojo():
        return render_template('dojo.html')
        name = request.form['name']
        email = request.form['email']



app.run(debug=True)
