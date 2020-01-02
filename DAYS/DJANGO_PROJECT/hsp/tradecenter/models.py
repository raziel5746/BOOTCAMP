from django.db import models


class Card(models.Model):
    title = models.CharField(max_length=150)
    rarity = models.CharField(max_length=30)
    card_class = models.CharField(max_length=30)
    card_type = models.CharField(max_length=30)
    api_id = models.CharField(max_length=30)
    image = models.ImageField(upload_to="gallery/", max_length=500)

    def __str__(self):
        return(f"{self.title}")


class UserCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField()

    def __str__(self):
        return(f"{self.amount}x{self.card} - {self.user}")


class Deck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return(f"Deck belonging to {self.user}")


class Transactions(models.Model):

    CURRENCY = [
        ('CARD', 'Card'),
        ('CREDITS', 'Credits'),
    ]

    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    card_bought = models.ForeignKey(Card, on_delete=models.CASCADE)
    currency = models.CharField(max_length=7,
                                choices=CURRENCY,
                                default='CARD')
    currency_amount =
    status = 
    pass