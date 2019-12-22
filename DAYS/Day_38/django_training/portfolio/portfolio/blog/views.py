from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return render(request, "Hello! Welcome to this Blog's Index.", {})

def index(request):
    return HttpResponse("<h1>Welcome to Home!</h1>")