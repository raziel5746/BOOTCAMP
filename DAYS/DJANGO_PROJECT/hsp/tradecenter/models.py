from django.db import models


class Card(models.Model):
    title = models.CharField(max_length=150)
    type = models.CharField(max_length=30)
    rarity = models.CharField(max_length=30)
    card_class = models.CharField(max_length=30)
    card_type = models.CharField(max_length=30)
    api_id = models.CharField(max_length=10)

    def __str__(self):
        return(f"{self.title}")

