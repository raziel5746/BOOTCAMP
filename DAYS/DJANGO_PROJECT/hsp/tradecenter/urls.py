from django.urls import path
from . import views

urlpatterns = [
    path('populator/cards/', views.cards_populator, name='cards-populator'),
    path('populator/images/', views.images_populator, name='images-populator'),
    path('populator/card_deleter/', views.cards_deleter, name='cards-deleter'),
    path('populator/hp_deleter/', views.heroe_powers_deleter, name='images-deleter'),
    path('populator/image_to_card/', views.image_to_card, name='image-to-card'),

    path('home/', views.home, name='tradecenter-home'),
    path('redeem30/', views.redeem30, name='redeem30'),
]