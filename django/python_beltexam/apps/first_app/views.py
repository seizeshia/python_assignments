from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import Users, Trips
from django.contrib import messages
from django.contrib.auth import logout
import datetime

def index(request):
    return render(request, 'first_app/index.html')

def registration(request):
    context={
    'f_name':request.POST['first_name'],
    'l_name':request.POST['last_name'],
    'email':request.POST['email'],
    'password':request.POST['password'],
    'confirm':request.POST['password_conf']
    }

    registerresults = Users.objects.creating(context)
    if registerresults['user'] != None:
        request.session['users']=registerresults['user'].id
        return redirect('/tripdash')
    else:
        for error in registerresults['registererrors']:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/')

    # for error in result['errors']:
    #         message.add_message(request messages.ERROR, errors)
    #         return redirect('/')

    return render(request, "first_app/registration")

def login(request):
    data={
    'email': request.POST['logemail'],
    'password':request.POST['password']
    }
    result= Users.objects.login(data)
    if result['loginerrors']==None:
        request.session['users']=result['users'].id
        return redirect('/profile')
    else:
        for loginerror in result['loginerrors']:

            messages.add_message(request, messages.ERROR, loginerror)
            return redirect('/')

def addtrip(request):
    data={
    'destination':request.POST['destination'],
    'plan':request.POST['plan'],
    'startdate':request.POST['sdate'],
    'enddate':request.POST['edate'],
    'userid':request.session['users']
    }
    canwetravel = Trips.objects.addtrip(data)
    if canwetravel['errors'] ==None:
        return redirect('/tripdash')
    else:
        for triperror in canwetravel['errors']:
            messages.add_message(request, messages.ERROR, triperror)
        return redirect('/trippage')

def trippage(request):
    return render(request, "first_app/createtrip.html")

def join(request):
    Trips.objects.create(user_id=Users.objects.get(id=request.session['users']))
    return redirect('/trippage')

def details(request, id):
    id = id
    data={
    'info': Trips.objects.filter(id=id)
    }
    return render(request, "first_app/tripdeets.html", data)

def tripdash(request):
    id=request.session['users']
    user = Users.objects.get(id=int(id))
    print user
    mytrips= Trips.objects.filter(id=int(id))
    print mytrips
    # print user
    # print Users.objects.filter(id=id).values('name')

    context={
    'first':user.f_name,
    'last':user.l_name,
    'email':user.email,
    'trips':Trips.objects.all(),
    'mytrips': mytrips
    }
    return render(request, "first_app/tripdash.html", context)
