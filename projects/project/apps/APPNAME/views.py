# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User, UserManager, Message, MessageManager, Comment, CommentManager
import datetime

# Create your views here.
def index(request):
    if 'user_id' not in request.session:
        return render(request, 'APPNAME/index.html')
    else:
        return render(request, 'APPNAME/home.html')

def register(request):
    data = {
    'first_name':request.POST['reg_first_name'],
    'last_name':request.POST['reg_last_name'],
    'username':request.POST['reg_username'],
    'password':request.POST['reg_password'],
    'confirm_password':request.POST['reg_confirm_password'],
    }
    new_user = User.objects.register(data)
    if new_user['errors_list']:
        for error in new_user['errors_list']:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/')
    else:
        messages.add_message(request, messages.ERROR, "Successfully Registered!")
        return redirect('/')

def login(request):
    data = {
    'username':request.POST['login_username'],
    'password':request.POST['login_password'],
    }
    user = User.objects.login(data)
    if user['errors_list']:
        for error in user['errors_list']:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/')
    else:
        request.session['user_id']=user['logged_user'].id
        request.session['first_name']=user['logged_user'].first_name
        request.session['last_name']=user['logged_user'].last_name
        return redirect('/')

def messageboard(request):
    messages_list=[]
    comments_list=[]
    for message in Message.objects.all():
        messages_list.append(message)
    for comment in Comment.objects.all():
        comments_list.append(comment)
    data = {
    "messages_list":messages_list,
    "comments_list":comments_list,
    }
    return render(request, 'APPNAME/messageboard.html', data);


def new_message_process(request):
    this_user = User.objects.get(id=request.session['user_id'])
    data = {
    'message':request.POST['message'],
    'this_user':this_user,
    }
    new_message=Message.objects.add(data)
    if new_message['errors_list']:
        for error in new_message['errors_list']:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/messageboard')
    else:
        messages.add_message(request, messages.ERROR, "Posted!")
        return redirect('/messageboard')

def new_comment_process(request, message_id):
    this_user = User.objects.get(id=request.session['user_id'])
    this_message = Message.objects.get(id=message_id)
    data = {
    'comment':request.POST['comment'],
    'this_user':this_user,
    'this_message':this_message,
    }
    new_comment=Comment.objects.add(data)
    if new_comment['errors_list']:
        for error in new_comment['errors_list']:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/messageboard')
    else:
        messages.add_message(request, messages.ERROR, "Commented!")
        return redirect('/messageboard')

def logout(request):
    request.session.clear()
    return redirect('/')
