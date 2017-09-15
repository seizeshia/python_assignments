from flask import Flask, render_template, request, redirect, session
app = flask(__name__)
app.secret_key = "ThisisSecret"

@app.route('/')
def index():
    return render_template('index.html')
