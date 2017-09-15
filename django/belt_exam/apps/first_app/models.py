# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re, bcrypt, datetime
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

class TripsManager(models.Manager):
    def addingtrip(self, data):
        errors=[]
        if data['destination']== "":
            errors.append("Your destination cannot be empty!")
        if data['desc']=="":
            errors.append("your Description cannot be empty")
        if len(data['start'])==0:
            errors.append("your startdate cannot be empty")
        if len(data['end'])==0:
            errors.append("Your End date cannot be empty")
        elif datetime.datetime.strptime(data['start'], '%Y-%m-%d')<= datetime.datetime.now():
            errors.append("Your trip cant be in the past")
        elif datetime.datetime.strptime(data['start'], '%Y-%m-%d')>= datetime.datetime.strptime(data['end'], '%Y-%m-%d'):
            errors.append("Your start date must come before your end date")
        if len(errors)==0:
            newtrip=Trips.objects.create(user_id = Users.objects.get(id=data['usersid']), destination=data['destination'], plan=data['desc'], startdate=data['start'], enddate=data['end'])
            trip = Tripsofusers.objects.create(userid= Users.objects.get(id=data['usersid']), tripid= Trips.objects.get(id=newtrip.id))

            return{'errors':None}
        else:
            return {'errors':errors}

class Users(models.Model):
    first=models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    created_at= models.DateTimeField(auto_now_add = True)
    objects= UserManager()

class Trips(models.Model):
    user_id= models.ForeignKey(Users, related_name="userid_trip")
    destination=models.CharField(max_length=50)
    plan=models.CharField(max_length=50)
    startdate=models.DateField()
    enddate=models.DateField()
    objects= TripsManager()

class Tripsofusers(models.Model):
    userid=models.ForeignKey(Users, related_name="userlink")
    tripid=models.ForeignKey(Trips, related_name="tripkey")
