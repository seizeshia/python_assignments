# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import Users
from django.contrib import messages
from django.contrib.auth import logout


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
        return render(request, 'first_app/tripdash.html', data)

def tripdash(request):
    if 'user' not in request.session:
        return redirect('/')
    id=request.session['user']
    user = Users.objects.get(id=int(id))


    data={
    'loggeduser':user.first,

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
