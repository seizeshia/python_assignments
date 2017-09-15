# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Posts

# Create your views here.
def index(request):

    data={
    'posts':Posts.objects.all()
  }
    return render(request, 'first_app/index.html', data)

def posting(request):
    data={
    'currentpost':request.POST['postcontent']
    }
    Posts.objects.posting(data)
    return redirect('/')
