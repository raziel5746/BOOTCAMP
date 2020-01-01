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
