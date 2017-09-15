from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'sayinghelloworld/index.html')

def show(request):
    print request.method
    return render(request, 'sayinghelloworld')
