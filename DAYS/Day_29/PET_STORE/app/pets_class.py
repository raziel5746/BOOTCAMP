import json

class Pet:
    def __init__(self):
        self.pets_list = []

    def return_pets(self):
        with open('app/all_pets.json', 'r') as f:
            pets_dict = json.load(f)
            self.pets_list = pets_dict['pets']
        return self.pets_list

    def return_pet(self, pet_id):
        if self.pets_list == []:
            print("LIST CREATED")
            self.return_pets()
        else:
            print("LIST ALREADY EXISTS")
        
        for pet in self.pets_list:
            if pet['id'] == pet_id:
                return pet
        else:
            print("PET NOT FOUND")
