# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import Users, Posts, Likes
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')

def register(request):
    context={
    'f_name':request.POST['first_name'],
    'l_name':request.POST['last_name'],
    'email':request.POST['email'],
    'password':request.POST['password'],
    'confirm':request.POST['password_conf']
    }

    registerresults = Users.objects.creating(context)
    if registerresults['user'] != None:
        request.session['user_id']=registerresults['user'].id
        return redirect('/profile')
    else:
        for error in registerresults['registererrors']:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/')
# def profile(request, id):
#     userinfo = User.objects.filter(id=request.session['id'])
#     return render(request, "first_app/profile.html")


def login(request):
    data={
    'email':request.POST['loginemail'],
    'password':request.POST['loginpassword']
    }
    loginresults= Users.objects.loginveri(data)
    if loginresults['users'] != None:
        request.session['user_id']=loginresults['users'].id
        return redirect('/wall')
    else:
        for error in loginresults['loginerrors']:
            messages.add_message(request, messages.ERROR, error)
            return redirect('/')

def logout(request):
    request.session.flush()
    return HttpResponse('Thank you for visiting.  You are now logged out!')

# def profile(request):
#     id=request.session['user_id']
#     user = Users.objects.get(id=int(id))
#
#
#     context={
#     'first':user.f_name,
#     'last':user.l_name,
#     'email':user.email,
#     'created':user.created_at
#     }
#
#     return render(request, "first_app/profile.html", context)

def post(request):
    id=request.session['user_id']
    user = Users.objects.get(id=int(id))
    all_posts =Posts.objects.all().order_by('-created_at')[:3]
    post_list=[]
    for post in all_posts:
        post.liked=True
        posts.num_likes = Likes.objects.filter(posts=posts).count()
        try:
            Likes.objects.get(user=data['user_id'], post=post)
        except:
            posts.liked=False
        post_list.append(posts)

    data={
    'postconts':request.POST['posting'],
    'user_id':user.id,
    'posts': post_list,
    }
    Posts.objects.creatingpost(data)
    print Posts.objects.all()
    return redirect('/wall', data)

def wall(request):
    id = request.session['user_id']
    user= Users.objects.get(id=int(id))

    data={
     'user_id':user.id,
     'postcont':Posts.objects.all(),
     'user_fname':user.f_name,

    #  'poster_fname':statuss.users_posts.f_name,
    #  'poster_lname':statuss.users_posts.l_name,
    #  'posted_on':statuss.created_at,
    }



    return render(request, "first_app/wall.html", data)

def likes(request):
    if request.method== "POST":
        a_post= Meetups.objects.get(id=post_id)
        a_user = User.objects.get(id=request.session['user_id'])
        Likes.objects.create(post=a_post, user=a_user)
        return redirect('/wall')
    # user= Users.objects.get(id=request.session['user_id'])
    #
    # data={
    # 'user_id':user.id,
    # 'post_id':request.POST['postid'],
    # }
    #
    # likers= Likes.objects.likeit(data)
    #
    # try:
    #     Posts.objects.get(user=data['user_id'], post_id=data['post_id'])
    #     messages.add_message('You cant like this again')
    #     return redirect('/wall')
    # except:
    #     Likes.objects.create(user= Users.objects.get(id=data['user_id']), post_id= Posts.objects.get(id=data['post_id']))
    #     liking=Posts.objects.get(id=data['post_id'])
    #     liking.count += 1
    #     liking.save()
    #     return redirect('/wall')
