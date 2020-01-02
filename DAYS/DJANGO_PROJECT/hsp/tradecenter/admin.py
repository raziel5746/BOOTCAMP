from django.contrib import admin
from .models import Card, UserCard, Deck, Transaction


admin.site.register(Card)
admin.site.register(UserCard)
admin.site.register(Deck)
admin.site.register(Transaction)
