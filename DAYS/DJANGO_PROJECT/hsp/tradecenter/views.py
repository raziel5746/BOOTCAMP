from django.shortcuts import render, redirect
from . import populator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Max, Min
from random import randint


def cards_populator(request):
    populate_cards()
    message = {'message': "Cards populated"}
    return render(request, 'tradecenter/populator.html', message)


def images_populator(request):
    populate_images()
    message = {'message': "Images populated"}
    return render(request, 'tradecenter/populator.html', message)


def cards_deleter(request):
    delete_cards_without_image()
    message = {'message': "Cards with no images, deleted"}
    return render(request, 'tradecenter/populator.html', message)


def heroe_powers_deleter(request):
    delete_heroe_powers()
    message = {'message': "Heroe Powers deleted"}
    return render(request, 'tradecenter/populator.html', message)


def image_to_card(request):
    insert_image_into_card()
    message = {'message': "Images added to cards"}
    return render(request, 'tradecenter/populator.html', message)


def home(request):
    if not request.user.usercard_set.all():
        redeem_cards = True
    else:
        redeem_cards = False
    redeem = {'redeem_cards': redeem_cards}
    return render(request, 'tradecenter/home.html', redeem)


def get_random(Model):

    # min_id = Model.objects.all().aggregate(min_id=Min("id"))['min_id']
    max_id = Model.objects.all().aggregate(max_id=Max("id"))['max_id']
    while True:
        pk = randint(1, max_id)
        record = Model.objects.filter(pk=pk).first()
        if record:
            return record


@login_required
def redeem30(request):
    user = request.user
    if not user.usercard_set.all():
        for i in range(30):
            card = get_random(Card)
            if user.usercard_set.filter(card=card).exists():
                card_to_add = user.usercard_set.get(card=card)
                card_to_add.amount += 1
                card_to_add.save()
            else:
                card_to_add = user.usercard_set.create(card=card)
                card_to_add.save()
    return redirect('tradecenter-home')


def my_cards(request):
    user_cards = request.user.usercard_set.all()
    print(user_cards)
    cards = {'cards': user_cards}
    return render(request, 'tradecenter/my_cards.html', cards)