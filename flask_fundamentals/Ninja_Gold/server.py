from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisisSecret"

gold =
@app.route('/')
def index():
    try:
        session["goldlevel"]
    else:
        session['goldlevel'] = 0
    # session["activities"]
    try:
        session['activities']
    except:
        sesssion["activites"] =""
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['location'] == 'farm':
        session['gold'] += rand.randrange(10,21)

    print "this is your total gold:"
    # to request a form inpit
    # request.form['locaiton']  the name value for the input
    return redirect('/')
app.run(debug=True)
