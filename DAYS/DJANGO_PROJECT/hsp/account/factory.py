from faker import Faker
from django.contrib.auth.models import User

fake = Faker()


def fake_user(num):

    for i in range(num):
        user = User(email=fake.email(),
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    username = fake.word()+"-"+fake.word(),)
        print(user.username)

        user.save()