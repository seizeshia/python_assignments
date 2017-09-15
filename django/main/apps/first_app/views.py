
# Create your views here.

from django.shortcuts import render, HttpResponse
# the index function is called when root is vitited
def index(request):
    print "*"*50
    return render(request, "templates/first_app/index.html" )
