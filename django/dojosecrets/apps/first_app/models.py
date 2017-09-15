# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UsersManager(models.Manager):
    def creating(self, data):
        registererrors=[]
        if data['f_name'] =="":
            registererrors.append("Name fields cannot be blank")
        if len(data['f_name'])<2:
            registererrors.append("First Name must be greater than two charectors")
        if len(data['l_name'])<2:
            registererrors.append("Last Name cannot be less than 2 charectors")
        if not data['f_name'].isalpha():
            registererrors.append("name fields can only have aphabetical charectors")
        if not EMAIL_REGEX.match(data['email']):
            registererrors.append("email format is incorrect")
        if data['password'] != data['confirm']:
            registererrors.append("Passwords do not match")
        if len(data['password'])<4:
            registererrors.append('password must be longer than 4 charectors')
        try:
            Users.objects.get(email=data['email'])
            registererrors.append("you already have an account!")
        except:
            pass
        if len(registererrors)==0:
            user = Users.objects.create(f_name=data['f_name'], l_name=data['l_name'], email=data['email'], password=data['password'])
            return {'user':user, 'registererrors':None}
        else:
            return {'user':None, 'registererrors':registererrors}

    def loginveri(self, data):
        loginerror = []
        try:
            user = Users.objects.get(email=data['email'])
            pass
        except:
            loginerrors.append("you dont have an account! Please register")
            return {'users':None, 'loginerrors':loginerrors}
        if user.password == data['password']:
            pass
        else:
            loginerror.append("Password is incorrect")
        if len(loginerror) == 0:
            return {'users':user, 'loginerrors':None}
        else:
            return {'users':None, 'loginerrors':loginerrors}


class PostsManager(models.Manager):
    def creatingpost(self, data):
        Posts.objects.create(postcontent= data['postconts'], users_posts= Users.objects.get(id=data['user_id']), count=int(0))
        return "apples"

class Users(models.Model):
    f_name= models.CharField(max_length=50)
    l_name= models.CharField(max_length=50)
    email= models.CharField(max_length=30)
    password= models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects= UsersManager()


class Posts(models.Model):
    postcontent= models.TextField()
    users_posts= models.ForeignKey(Users, related_name="whoposted")
    created_at = models.DateTimeField(auto_now_add=True)
    count = models.BigIntegerField()
    objects = PostsManager()

class Likes(models.Model):
    user= models.ForeignKey(Users, related_name="userid")
    post= models.ForeignKey(Posts, related_name="user_like")
