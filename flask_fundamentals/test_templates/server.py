from flask import flask, render_template
app = flask(__name__)
@app.reoute('/')
def index():
    return render_template("index.html",phase="hello", times=5)
app.run(debug=True)
