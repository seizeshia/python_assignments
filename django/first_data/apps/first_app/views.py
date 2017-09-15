from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from .models import Product
import random
import string
# Create your views here.
def index(request):
    Product.objects.create(name="bike", weight="100", prices="300", cost="200", category="toys" )
    Product.objects.create(name="scooter", weight="10", prices="120", cost="30", category="toys")
    Product.objects.create(name="kite", weight="1", prices="45", cost="10", category="toys")
    product = Product.objects.all()
    print product
    return render(request, "first_app/index.html")
