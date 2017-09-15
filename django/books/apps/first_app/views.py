from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

def index(request):
    Books.objects.create(title="Harry Potter", author="J.K. Rowling", published_date="2010", category="fiction")
    Books.objects.create(title="Hooked", author="Nir Eyal", published_date="2012",category="non-fiction")
    Books.objects.create(title="The Lean Startup", author="Steve Blank", published_date="2013-08-13", category="non-fiction")
    return render(request, "first_app/index.html")
# Create your views here.
