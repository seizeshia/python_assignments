# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re, bcrypt, datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class TripsManager(models.Manager):
    def addtrip(self,data):
        triperrors=[]
        if data['destination'] == "":
            triperrors.append("destination cannot be empty!")
        if data['plan']=="":
            triperrors.append("Trip description cannot be empty!")
        if data['startdate']=="":
            triperrors.append('startdate cannot be empty')
        if data['enddate']=="":
            triperrors.append('enddate cannot be empty')
        elif datetime.datetime.strptime(data['startdate'], '%Y-%m-%d') >= datetime.datetime.strptime(data['enddate'], '%Y-%m-%d'):
            triperrors.append('End date needs to come after the start date!')
        elif datetime.datetime.strptime(data['startdate'], '%Y-%m-%d') <= datetime.datetime.now():
            triperrors.append('trip start date needs to be in the future')
        if len(triperrors)==0:
            Trips.objects.create(user_id= Users.objects.get(id=data['userid']), destination=data['destination'], plan=data['plan'], startdate=data['startdate'],enddate=data['enddate'])
            return {'errors':None}
        else:
            return {'errors':triperrors}

class UserManager(models.Manager):
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
            user = Users.objects.create(f_name=data['f_name'],l_name=data['l_name'],email=data['email'],password=data['password'])
            return {'user':user, 'registererrors':None}
        else:
            return {'user':None, 'registererrors':registererrors}
    def login(self,data):
        loginerrors=[]
        # user=Users.objects.get(email = data['email'])
        try:
            user= Users.objects.get(email=data['email'])
            pass
        except:
            loginerrors.append("You do not have an account!  Please register")
            return {'users':None, 'loginerrors': loginerrors}

        print user

        if user.password == data['password']:
            pass
        else:
            loginerrors.append("Password is incorrect!")
        if len(loginerrors) == 0:
            return {'users':user, 'loginerrors':None}
        else:
            return {'users':None, 'loginerrors': loginerrors}

# Create your models here.

class Users(models.Model):
    f_name= models.CharField(max_length=50)
    l_name= models.CharField(max_length=50)
    email= models.CharField(max_length=30)
    password= models.CharField(max_length=10)
    objects= UserManager()

class Trips(models.Model):
    user_id= models.ManyToManyField(Users, related_name="user_id")
    destination= models.CharField(max_length=50)
    startdate= models.DateField()
    enddate=models.DateField()
    plan=models.CharField(max_length=100)
    objects=TripsManager()
