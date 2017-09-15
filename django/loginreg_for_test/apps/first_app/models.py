# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re, bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def register(self, data):
        errors=[]
        if len(data['first']) < 2:
            errors.append('First name cannot be less than 2 letters')
        if len(data['last']) <2:
            errors.append('Last Name cannot be less than two letters')
        if not data['first'] .isalpha():
            errors.append('name fields must only be letters')
        if not EMAIL_REGEX.match(data['email']):
            errors.append('email is not in the right format')
        if data['password'] != data['password_conf']:
            errors.append('passwords do not match')
        if len(data['password'])<4:
            errors.append('passwords cannot be less than 4 charectors')
        try:
            Users.objects.get(email=data['email'])
            errors.append('You are already registered!')
        except:
            pass
        if len(errors)==0:
            data['password'] = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
            user = Users.objects.create(first=data['first'], last=data['last'],email=data['email'],password=data['password'])
            return {'user':user, "errors":None}
        else:
            return{'user':None, 'errors':errors}

    def login(self,data):
        errors=[]
        if data['email']=="":
            errors.append('email is missing!')
        if not EMAIL_REGEX.match(data['email']):
            errors.append('email is not in the right format')
        try:
            user=Users.objects.get(email=data['email'])
            if bcrypt.hashpw(data['password'].encode('utf-8'), user.password.encode('utf-8')) != user.password.encode('utf-8'):
                errors.append("Incorrect password")
        except:
            errors.append("incorrect password")

        if len(errors)== 0:
            return {'user':user, 'errors':None}
        else:
            return {'errors':errors}




class Users(models.Model):
    first=models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    created_at= models.DateTimeField(auto_now_add = True)
    objects= UserManager()
