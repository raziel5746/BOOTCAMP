from tradecenter.models import Card
import json
import requests
from os import path, remove


def populate_cards():

    with open('tradecenter/static/cards.json') as f:
        cards = json.load(f)

        for card in cards:
            if 'rarity' in card:
                new_card = Card(title=card['name'], rarity=card['rarity'], card_class=card['cardClass'], card_type=card['type'], api_id=card['id'])
                new_card.save()
            elif 'cardClass' in card:
                new_card = Card(title=card['name'], rarity="FREE", card_class=card['cardClass'], card_type=card['type'], api_id=card['id'])
                new_card.save()
            else:
                new_card = Card(title=card['name'], rarity="FREE", card_class="CLASSLESS", card_type=card['type'], api_id=card['id'])
                new_card.save()
    return

def populate_images():
    cards = Card.objects.all()
    for card in cards:
        image_url = f"https://art.hearthstonejson.com/v1/render/latest/enUS/256x/{card.api_id}.png"
        response = requests.get(image_url)
        
        if response.status_code == 200:
            image_file = requests.get(image_url, allow_redirects=True)
            open(f"/home/raziel/Documents/BOOTCAMP/DAYS/DJANGO_PROJECT/hsp/media/gallery/{card.api_id}.png", 'wb').write(image_file.content)
            print(f"Image added to '{card}' card.")
        else:
            card.delete()
            print(f"Card '{card}' deleted.")


def delete_cards_without_image():
    cards = Card.objects.all()
    for card in cards:
        if path.exists(f"/home/raziel/Documents/BOOTCAMP/DAYS/DJANGO_PROJECT/hsp/media/gallery/{card.api_id}.png"):
            pass
        else:
            print(f"BBBBBBBBBBBBBBB- FILE {card.api_id}.png DOES NOT EXIST.")
            card.delete()
            print("Card deleted successfully")


def delete_heroe_powers():
    cards = Card.objects.filter(card_type="HERO_POWER")
    for card in cards:
        remove(f"/home/raziel/Documents/BOOTCAMP/DAYS/DJANGO_PROJECT/hsp/media/gallery/{card.api_id}.png")
        print(f"BBBBBBBBBBBBBBB- FILE {card.api_id}.png REMOVED.")
        card.delete()
        print("Card deleted successfully")


def insert_image_into_card():
    cards = Card.objects.all()
    counter = 0
    for card in cards:
        counter += 1
        card.image = f"gallery/{card.api_id}.png"
        card.save()
    else:
        print(f"Added {counter} images")
