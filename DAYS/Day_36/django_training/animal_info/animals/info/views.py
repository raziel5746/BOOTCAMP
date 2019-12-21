from django.shortcuts import render
import json


def index(request):
    return render(request, 'index.html')


def family(request, id):
    with open('info/animals.json', 'r') as f:
        my_file = json.load(f)
        animals = my_file['animal']
        families = my_file['family']
        for animal in animals:
            if animal['id'] == id:
                my_animal = animal
    return render(request, 'family.html', {'id': id})


def animal(request, id):
    with open('info/animals.json', 'r') as f:
        my_file = json.load(f)
        animals = my_file['animal']
        families = my_file['family']
        for animal in animals:
            if animal['id'] == id:
                my_animal = animal

        for family in families:
            if family['id'] == my_animal['family']:
                my_animal_family = family['name']

    return render(request, 'animal.html', {'id': id, 'animal': my_animal, 'family': my_animal_family})
