from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key='ThisisSecret'
# tried to run the test function within the next function in order to get the result but it didnt work...
#
# def test():
#     if  session['guess'] == session['thenumber']:
#         result = 'winner'
#         return render_template("index.html", result=result)
#     elif session['guess'] > session['thenumber']:
#         result = 'lower'
#         return render_template("index.html", result=result)
#     elif session['guess'] < session['thenumber']:
#         result = 'higher'
#         return render_template("index.html", result=result)


@app.route('/')
def index():
    session['thenumber'] = random.randrange(0, 101)
    print session['thenumber']
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def next():
    session['guess']=int(request.form['guess'])
    print 'guess'
    if  session['guess'] == session['thenumber']:
        result = 'winner'
        return render_template("index.html", result=result)
    elif session['guess'] > session['thenumber']:
        result = 'lower'
        return render_template("index.html", result=result)
    elif session['guess'] < session['thenumber']:
        result = 'higher'
        return render_template("index.html", result=result)
    return redirect('/')

@app.route('/playagain')
def playagain():
    index()
    return redirect('/')

# @app.route('/guess')
# def guess():
#     guess = int(request.form['guess'])
#     print guess
#     test()
#     return redirect('/')
app.run(debug=True)
