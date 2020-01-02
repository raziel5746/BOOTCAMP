from django.db import models
from django.contrib.auth.models import User


class Card(models.Model):
    title = models.CharField(max_length=150)
    rarity = models.CharField(max_length=30)
    card_class = models.CharField(max_length=30)
    card_type = models.CharField(max_length=30)
    api_id = models.CharField(max_length=30)
    image = models.ImageField(upload_to="gallery/", max_length=500)

    def __str__(self):
        return(f"{self.title}")


class Deck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return(f"Deck belonging to {self.user}")


class UserCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField(default=1)
    # deck = models.ForeignKey(Deck, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return(f"{self.amount} x {self.card} - {self.user}")


class Transaction(models.Model):

    CURRENCY = [
        ('CARD', 'Card'),
        ('CREDITS', 'Credits'),
    ]

    STATUS = [
        ('PENDING', 'Pending'),
        ('EXECUTED', 'Executed'),
    ]

    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyers')
    card_bought = models.ForeignKey(Card, on_delete=models.CASCADE)
    currency = models.CharField(max_length=7,
                                choices=CURRENCY,
                                default='CARD')
    currency_amount = models.SmallIntegerField()
    status = models.CharField(max_length=8,
                                choices=STATUS,
                                default='PENDING')
