from django.shortcuts import render
from tradecenter.populator import populate


def populator(request):
    populate()
    return render(request, 'tradecenter/populator.html')