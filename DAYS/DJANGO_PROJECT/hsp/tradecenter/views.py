from django.shortcuts import render
from tradecenter.populator import populate_cards, populate_images, delete_cards_without_image, delete_heroe_powers, insert_image_into_card


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
