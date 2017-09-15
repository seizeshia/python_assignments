from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisisSecret"

def counterhere(num):
  try:
    session['count'] += num
  except KeyError:
    session['count'] = num

def plustwo():
    session['count']+= num


@app.route('/')
def index():
'''
This is my doc string
'''
    try:
        increment_value = int(request.args['count'])
    except KeyError:
        increment_value = 1

    counterhere(increment_value)
    return render_template('index.html')
#
#
# # @app.route('/users', methods=['POST'])
# # def increment():
# #     count += 1
# #     return redirect('/')
#
# @app.route('/plustwo', methods=['POST'])
# def addtwo():
#     plustwo()
#     return redirect('/')

@app.route('/zeroout', methods=['POST'])
def zeroout():
    session['count']=0
    return redirect('/')


app.run(debug=True) # run our server
