# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import Users, Quotes, Quotesofusers
from django.contrib import messages
from django.contrib.auth import logout


# Create your views here.
def index(request):
    
    return render(request, 'first_app/index.html')

def register(request):

    data={
    'name':request.POST['name'],
    'alias':request.POST['alias'],
    'email':request.POST['email'],
    'password':request.POST['password'],
    'password_conf':request.POST['password_conf'],
    'dob':request.POST['dob']
    }

    reg= Users.objects.register(data)

    if reg['errors'] != None:
        for error in reg['errors']:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/')

    else:
        request.session['user']=reg['user'].id
        return redirect('/quotedash')

def quotedash(request):
    if 'user' not in request.session:
        return redirect('/')

    id=request.session['user']
    user = Users.objects.get(id=int(id))
    myquotes=Quotes.objects.filter(quotelink__userid=user)
    othersquotes=Quotes.objects.exclude(quotelink__userid=user)

    data={
    'loggeduser':user.name,
    'mine':myquotes,
    'others':othersquotes,
    }
    return render(request, "first_app/quotedash.html", data)

def favorite(request,id):
    me= Users.objects.get(id=request.session['user'])
    thequote= Quotes.objects.get(id=id)
    Quotesofusers.objects.create(userid=me, quoteid=thequote)
    return redirect('/quotedash')

def removefav(request,id):
    me= Users.objects.get(id=request.session['user'])
    thequote= Quotes.objects.get(id=id)
    Quotesofusers.objects.filter(userid=me, quoteid=thequote).delete()
    return redirect('/quotedash')
def quoteprofile(request,id):
    quote=Quotes.objects.filter(quotelink__userid=id)
    userr=Users.objects.get(id=id)

    data={
    'quotes':quote,
    'name':userr,
    }
    return render(request, "first_app/quoteprofile.html", data)

def addquote(request):
    id=Users.objects.get(id=request.session['user'])
    data={
    'quote':request.POST['myquote'],
    'quotedby':request.POST['quotedby'],
    'userid':request.session['user'],
    }
    quoteveri=Quotes.objects.addingquote(data)
    if quoteveri['errors']==None:
        return redirect('/quotedash')
    else:
        for error in quoteveri['errors']:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/quotedash')

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
            return redirect('/quotedash')
    else:
        for error in login['errors']:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/')
