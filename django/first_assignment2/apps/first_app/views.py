# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
import random
import string


def index(request):

    return render(request, "first_app/index.html")

def processing(request, color):
    if color == 'red':
        context={
        "hue":"../../static/first_app/images/raphael.jpg"
        }
        # ../../static/first_app/images/raphael.jpg
    elif color == 'purple':
        context={
        'hue':"../../static/first_app/images/donatello.jpg"
        }
    elif color == 'blue':
        context={
        'hue':"../../static/first_app/images/leonardo.jpg"
        }
    elif color == 'orange':
        context={
        'hue': "../../static/first_app/images/michelangelo.jpg"
        }
    else:
        context={
        'hue':"../../static/first_app/images/april.jpg"
        }
    return render(request, "first_app/index.html", context)

def ninjas(request):
    return redirect('/')
