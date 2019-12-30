from tradecenter.models import Card
import json


def populate():

    with open('tradecenter/static/cards.json') as f:
        cards = json.load(f)

        print(cards[0]['name'])
        print(cards[1]['name'])
    return