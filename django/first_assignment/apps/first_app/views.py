# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from datetime import datetime
import random
import string


counter=0
word = ("apples", "oranges", "cherries", "grapes")
def index(request):
    context ={
    "randomword":random.choice(word),
    "counter":counter
    }


    return render(request, "first_app/index.html")

def randomize(request):
    if request.method == "POST":
        savethis=''.join((random.choice(session.POST['randomchar']) for i in range(14))
        print savethis
    # randomworddd= ''.join((random.choice(session.POST['randomchar']) for i in xrange(14)))
        # request.session['theword'] = request.POST['randomchar']
        # request.POST['randomchar']
        return redirect('/')

def projects(request):
    print (request.method)
    return render(request, 'first_app/projects.html')

def about_me(request):
    print (request.method)
    return render(request, 'first_app/about_me.html')

def new_user(request):
    if request.post == "POST":
        print "*"*50
        request.session['name'] = request.POST['first_name']
        return redirect('/')
    else:
        return redirect('/')

# Create your views here.
