import json


class Pet:
    def __init__(self):
        self.pets_list = []

    def return_pets(self):
        with open("all_pets.json", 'r') as f:
            pets_dict = json.load(f)
            for key in pets_dict:
                self.pets_list = pets_dict[key]
        return pets_list

    def return_pet(self, pet_id):
        if self.pets_list == []:
            print("LIST CREATED")
            self.return_pets()
        else:
            print("LIST ALREADY EXISTS")
        
        for pet in self.pets_list:
            if pet["id"] == pet_id:
                print(self.pets_list[pet_id])
                return self.pets_list[pet_id]
        else:
            print("PET NOT FOUND")

pets_list = Pet()
pets_list.return_pet(0)