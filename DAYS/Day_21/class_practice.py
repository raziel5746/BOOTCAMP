## EXERCISE 1

# class Dog:
#     def __init__(self, name_dog, height_dog):
#         self.name = name_dog
#         self.height = height_dog
#
#     def talk(self):
#         print("Woof!")
#
#     def jump(self):
#         print(self.height * 2)
#
#
# davids_dog = Dog("Rex", 50)
# sarahs_dog = Dog("Teacup", 20)
#
# if davids_dog.height > sarahs_dog.height:
#     davids_dog.winner = True
# else:
#     sarahs_dog.winner = True
# print(sarahs_dog.height)
# print(sarahs_dog.name)
#
# print(davids_dog.winner)


#=======================================================

# EXERCISE 2

class Zoo:
    def __init__(self, zoo_name):
        self.animals = ['bear', 'anaconda', 'baboon', 'horse', 'dolphin', 'deer', 'bees']
        self.name = zoo_name
        self.animals_pen = {}

    def addAnimal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def getAnimals(self):
        print(str(self.animals))

    def sellAnimal(self, animal):
        if animal in self.animals:
            print(f"Goodbye {animal}")
            self.animals.remove(animal)

    def sortAnimals(self):
        self.animals.sort()
        for animal in self.animals:
            if animal not in self.animals_pen.values():
                if animal[0] not in self.animals_pen:
                    self.animals_pen[animal[0]] = [animal]
                else:
                    self.animals_pen[animal[0]].append(animal)
        print(self.animals_pen)
