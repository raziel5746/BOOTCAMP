from django.shortcuts import render
# from django.http import HttpResponse
# from django.urls import reverse
from .models import Person


def index(request):
    # print(reverse('home'))
    return render(request, "phonebook/index.html")


def home(request):
    # print(f"Number : {number}")
    # print(reverse('home', args=[42]))
    return render(request, "phonebook/home.html")


def persons(request):
    person_list = Person.objects.order_by('last_name')
    return render(request, "phonebook/person_list.html", {'persons': person_list})


def person(request, id):
    person = Person.objects.get(id=id)
    return render(request, "phonebook/person_details.html", {'person': person})
