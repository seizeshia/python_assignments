# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UsersManager(models.Manager):
    def register(self, context):
        errors=[]
        if len(context['name'])<= 2:
            errors.append('name must be more than two letters')
        if context['password'] != context['password_conf']:
            errors.append('your passwords do not match')
        if context['email']== "":
            errors.append('You must fill in email section')
        elif not EMAIL_REGEX.match(context['email']):
            errors.append('Your email is not in the right format!')
        try:
            user = Users.objects.get(email=context['email'])
            errors.append('You already have an account, please login!')
            return {'users':users,'errors':errors}
        except:
            users.objects.create(name=context['name'], alias=context['alias'], email=context['email'], password=context['password'])
            return {'user':None}

    def login(self, data):
        errors=[]
        if


class Users(models.Model):
    name= models.CharField(max_length=50)
    alias= models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    password= models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects= UsersManager()

class Books(models.Model):
    book_names= models.CharField(max_length=100)
    author=models.CharField(max_length=50)
    user_deets=models.ForeignKey(Users, related_name="books_table")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Reviews(models.Model):
    ratings= models.IntegerField()
    user_related=models.ForeignKey(Users, related_name="userss")
    review= models.TextField(max_length=500)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
