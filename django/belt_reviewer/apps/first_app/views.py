# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import Users, Books, Reviews

def index(request):
    return render(request, 'first_app/index.html', context)

def register(request):
    context={
    'name':request.POST['name'],
    'alias':request.POST['alias'],
    'email':request.POST['email'],
    'password':request.POST['password'],
    'password_conf':request.POST['password_conf']
    }
    users= Users.objects.register(data)
    if users['user'] != None:
        for message in errors:
            message.add_messages(request,message.ERROR, message)
            #this may be wrong
            return redirect('/')
    if user['user'] == None:
        return redirect('/profile')


    return redirect('/')

def login(request):
    data={
    'email':request.POST['email'],
    'password':request.POST['password']
    }
    return redirect

def welcome(request):

    return render(request, 'first_app/welcome.html', data)
