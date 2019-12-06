from app.pets_class import Pet
import json

class Cart:
    def __init__(self):
        self.total = 0

    def add_to_cart(self, pet_id):
        '''Adds the ID and the PRICE of the chosen pet to the json file '''
        
        print("ADD_TO_CART EXECUTED")
        pet_obj = Pet()
        pet_to_add = pet_obj.return_pet(pet_id)

        with open("app/cart.json", "r") as f:
            cart = json.load(f)
        print(f"BEFORE: {cart}")

        cart['cart'].append({pet_to_add["id"]: pet_to_add["name"]})
        with open("app/cart.json", "w") as f:
            json.dump(cart, f)
        print(f"AFTER: {cart}")
        return cart


    def get_cart(self):
        pass

    def get_total(self):
        pass
