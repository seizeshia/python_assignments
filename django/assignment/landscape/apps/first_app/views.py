# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
import random
import string

def index(request):
    return render(request, "first_app/index.html")

def results(request, number):
    if int(number) >= 1 and int(number) <= 10:
        context={
        "season":'../../static/first_app/winter.jpg'
        }
        return render(request, "first_app/results.html", context)

    elif int(number) >10 and int(number) < 20:
        context={
        'season':'../../static/first_app/dessert.jpg'
        }
        return render(request, "first_app/results.html", context)
    elif int(number) >= 20 and int(number) <30:
        context={
        'season':'../../static/first_app/forrest.jpg'
        }
        return render(request, "first_app/results.html", context)
    elif int(number) >=30 and int(number) <40:
        context={
        'season':'../../static/first_app/vineyard.jpg'
        }
        return render(request, "first_app/results.html", context)
    elif int(number) >= 40 and int(number) < 50:
        context={
        'season':'../../static/first_app/tropics.jpg'
        }
        return render(request, "first_app/results.html", context)
