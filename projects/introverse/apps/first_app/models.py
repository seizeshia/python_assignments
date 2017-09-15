# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re, bcrypt, datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def register(self, data):
        errors=[]
        if len(data['name']) < 2:
            errors.append('name cannot be less than 2 letters')
        if len(data['alias']) <4:
            errors.append('alias cannot be less than 4 letters')
        if not data['name'] .isalpha():
            errors.append('name fields must only be letters')
        if not EMAIL_REGEX.match(data['email']):
            errors.append('email is not in the right format')
        if data['password'] != data['password_conf']:
            errors.append('passwords do not match')
        if len(data['password'])<4:
            errors.append('passwords cannot be less than 4 charectors')
        if data['dob']=="":
            errors.append('birth date cannot be empty')
        elif datetime.datetime.strptime(data['dob'], '%Y-%m-%d') >= datetime.datetime.now():
            errors.append("You are not born yet!")
        try:
            Users.objects.get(email=data['email'])
            errors.append('You are already registered!')
        except:
            pass
        if len(errors)==0:
            data['password'] = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
            user = Users.objects.create(name=data['name'], alias=data['alias'],email=data['email'],password=data['password'], birthday=data['dob'])
            # count=0
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

class QuotesManager(models.Manager):
    def addingquote(self,data):
        errors=[]
        if len(data['quote'])<10:
            errors.append('Your quote must be at least 10 charectors')
        if len(data['quotedby'])<3:
            errors.append('Quoted By must be more than 3 charectors')
        if len(errors)==0:
            newquote=Quotes.objects.create(user_id=Users.objects.get(id=data['userid']), quote=data['quote'], quotedby=data['quotedby'])
            connections= Quotesofusers.objects.create(userid=Users.objects.get(id=data['userid']), quoteid=Quotes.objects.get(id= newquote.id))
            # userinfo=Users.objects.get(id=data['userid'])
            # userinfo.count= userinfo.count+1
            return{'errors':None}
        else:
            return{'errors':errors}

class Users(models.Model):
    name=models.CharField(max_length=50)
    alias = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    # count= models.IntegerField()
    birthday =models.DateField()
    created_at= models.DateTimeField(auto_now_add = True)
    objects= UserManager()

class Quotes(models.Model):
    user_id=models.ForeignKey(Users, related_name="usersid")
    quote= models.CharField(max_length=255)
    quotedby=models.CharField(max_length=20)
    objects= QuotesManager()

class Quotesofusers(models.Model):
    userid= models.ForeignKey(Users, related_name="userlink")
    quoteid=models.ForeignKey(Quotes, related_name="quotelink")
