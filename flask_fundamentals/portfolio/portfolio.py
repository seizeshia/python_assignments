
from flask import Flask, render_template  # Import Flask to allow us to create our app, and import
                                          # render_template to allow us to render index.html.
app = Flask(__name__)                     # Global variable __name__ tells Flask whether or not we
                                          # are running the file directly or importing it as a module.
@app.route('/')                           # The "@" symbol designates a "decorator" which attaches the
def root():
    return render_template('root.html')    # Render the template and return it!

@app.route('/about') #can be taken here by going to localhost:5000/success
def success():
    return render_template('about.html')

@app.route('/projects') #can be taken here by going to localhost:5000/success
def projects():
    return render_template('projects.html')                                          # following function to the '/' route. This means that
    # whenever we send a request to localhost:5000/ we will run
app.run(debug=True)
