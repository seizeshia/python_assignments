from django.shortcuts import render, redirect, HttpResponse
from .models import Courses

def index(request):
    context={
    "courses": Courses.objects.all()
    }
    return render(request, "first_app/index.html", context)

def adding(request):
    Courses.objects.create(name=request.POST['name'], description= request.POST['description'])
    return redirect('/')

def removing(request, id):
    context={
    'course': Courses.objects.filter(id=id)
    }
    return render(request, "first_app/confirmation.html",context)
def delete(request,id):
    
    return redirect('/')
