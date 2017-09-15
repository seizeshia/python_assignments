# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import Users, Trips, Tripsofusers
from django.contrib import messages
from django.contrib.auth import logout
import datetime


# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')

def register(request):
    data={
    'first':request.POST['f_name'],
    'last':request.POST['l_name'],
    'email':request.POST['email'],
    'password':request.POST['password'],
    'password_conf':request.POST['password_conf']
    }

    reg= Users.objects.register(data)

    if reg['errors'] != None:
        for error in reg['errors']:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/')

    else:
        request.session['user']=reg['user'].id
        return redirect('/tripdash')
def tripinfo(request,id):
    trip = Trips.objects.get(id=id)
    me = Users.objects.get(id=request.session['user'])
    usersontrip=Tripsofusers.objects.filter(tripid=trip).exclude(userid=me)


    data={
    'id':id,
    'thistrip':trip,
    'usersontrip':usersontrip
    }

    return render(request, 'first_app/tripinfo.html', data)

def join(request,id):
    me = Users.objects.get(id=request.session['user'])
    trip = Trips.objects.get(id=id)
    Tripsofusers.objects.create(tripid=trip, userid=me)
    return redirect('/tripdash')

def pageadd(request):
    if 'user' not in request.session:
            return redirect('/')
    return render(request, 'first_app/adding.html')

def addingtrip(request):
    data={
    'destination':request.POST['destination'],
    'desc':request.POST['plan'],
    'start':request.POST['startdate'],
    'end':request.POST['enddate'],
    'usersid':request.session['user']
    }
    tripveri= Trips.objects.addingtrip(data)
    if tripveri['errors'] == None:
        return redirect('/tripdash')
    else:
        for error in tripveri['errors']:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/pageadd')

def tripdash(request):
    if 'user' not in request.session:
        return redirect('/')

    id=request.session['user']
    user = Users.objects.get(id=int(id))
    mytripss=Trips.objects.filter(tripkey__userid=user)
    mytrips=Trips.objects.filter(user_id=id)
    othertrips= Trips.objects.exclude(tripkey__userid=user)
    # othertrips= Trips.objects.exclude(user_id=int(id))

    data={
    'loggeduser':user.first,
    'mytrips':mytripss,
    'others':othertrips,
    }
    return render(request, "first_app/tripdash.html", data)

def logout(request):
    request.session.flush()
    return HttpResponse('Thank you for visiting.  You are now logged out!')

def login(request):
    data={
    'email':request.POST['email'],
    'password':request.POST['password']
    }

    login =Users.objects.login(data)

    if login['errors']==None:
            request.session['user'] = login['user'].id
            return redirect('/tripdash')
    else:
        for error in login['errors']:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/')
