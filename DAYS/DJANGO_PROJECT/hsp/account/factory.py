from faker import Faker
from django.contrib.auth.models import User
from tradecenter.models import Card
from django.db.models import Max, Min
from random import randint

fake = Faker()


def get_random(Model):

    # min_id = Model.objects.all().aggregate(min_id=Min("id"))['min_id']
    max_id = Model.objects.all().aggregate(max_id=Max("id"))['max_id']
    while True:
        pk = randint(1, max_id)
        record = Model.objects.filter(pk=pk).first()
        if record:
            return record


def fake_user(num):

    for i in range(num):
        user = User(email=fake.email(),
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    username = fake.word()+"-"+fake.word(),)
        print(user.username)

        user.save()


def add_cards():
    users = User.objects.all()
    for user in users:
        if not user.usercard_set.all():
            random_card = get_random(Card)
            for i in range(30):
                new_card = get_random(Card)
                if user.usercard_set.filter(card=new_card).exists():
                    card_to_add = user.usercard_set.get(card=new_card)
                    card_to_add.amount += 1
                    card_to_add.save()
                else:
                    card_to_add = user.usercard_set.create(card=new_card)
                    card_to_add.save()