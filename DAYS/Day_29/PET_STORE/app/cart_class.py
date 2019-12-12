from app.pets_class import Pet
import json
from flask import flash

class Cart:
    def __init__(self):
        self.total = 0
        self.pet_obj = Pet()
        

    def add_to_cart(self, pet_id):
        '''Adds the ID and the PRICE of the chosen pet to the json file '''
        
        pet_to_add = self.pet_obj.return_pet(pet_id)

        with open('app/cart.json', 'r') as f:
            cart = json.load(f)

        cart['cart'].append({'id':pet_to_add['id'], 'price':pet_to_add['price'], 'name':pet_to_add['name']})
        with open('app/cart.json', 'w') as f:
            json.dump(cart, f)
        return cart


    def added_alert(self):
        self.get_total()
        flash(f"Pet succesfully added to cart. New total value: ${self.total}")


    def get_cart(self):
        with open('app/cart.json', 'r') as f:
            cart = json.load(f)
            cart = cart['cart']
        return cart


    def get_total(self):
        cart = self.get_cart()
        pets_dict = self.pet_obj.return_pets()
        for item in cart:
            for pet in pets_dict:
                if item['id'] == pet['id']:
                    self.total += pet['price']
        return self.total

