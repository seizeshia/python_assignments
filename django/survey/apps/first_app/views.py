from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from datetime import datetime
import random
import string

def index(request):
    return render(request, "first_app/index.html")

def adding(request):
    request.session['name'] = request.POST['name']
    request.session['Location'] = request.POST['Location']
    request.session['Favorite'] = request.POST['Favorite']
    request.session['comment'] = request.POST['comment']
    return redirect(request, '/first_app/results.html')

def results(request):

    return render(request, "first_app/results.html")
