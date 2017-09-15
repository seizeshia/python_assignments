from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

@app.route('/')
def surveylanding():
    return render_template('surveylanding.html')


@app.route('/surveysubmit', methods=['post'])
def surveysubmit():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comments = request.form['comments']
    return render_template('/surveysubmit.html',name= name, location=location, language=language, comments=comments)

app.run(debug=True)
