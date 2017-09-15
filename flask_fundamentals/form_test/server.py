from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
    # we'll talk about the following two lines after we learn a little more
    # about forms
    name = request.form['name']
    email = request.form['email']
    # redirects back to the '/' route
    return redirect('/')
    my_datarequest.form
    app.run(debug=True) # run our server

# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
