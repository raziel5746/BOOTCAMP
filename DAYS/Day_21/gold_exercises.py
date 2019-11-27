# EXERCISE 1
# from math import pi
#
#
# class Circle:
#     def __init__(self, radius=1.0):
#         self.radius = radius
#         self.perimeter = None
#         self.area = None
#
#     def calcPerimeter(self):
#         self.perimeter = self.radius * 2 * pi
#
#     def calcArea(self):
#         self.area = self.radius ** 2 * pi
#
#     @staticmethod
#     def printDef():
#         print("A circle is the locus of all points equidistant from a central point. ")
#
# #===========================================================

# EXERCISE 2
#
# from faker import Faker
# fake = Faker()
#
#
# class MyList:
#     def __init__(self, list_arg=None):
#         self.my_list = list_arg
#
#     def reverseList(self):
#         reversed_list = self.my_list[::-1]
#         print(reversed_list)
#
#     def sortList(self):
#         print(self.my_list.sort())
#
#     def sameLen(self):
#         new_list = []
#         for el in self.my_list:
#             new_list.append(fake.name())
#         print(new_list)

# ==========================================================

# EXERCISE 3

# from random import random
# from random import randint
#
#
# class QuantumParticle:
#     def __init__(self):
#         self.x = randint(0, 50)
#         self.p = random() * 50
#         self.spin = round(random()) - 0.5
#
#     def measurePosition(self):
#         self.x = randint(0, 50)
#         self.p = random() * 50
#         self.spin = round(random()) - 0.5
#
#     def measureMomentum(self):
#         self.p = random() * 50
#         self.x = randint(0, 50)
#         self.spin = round(random()) - 0.5
#
#     def measureSpin(self):
#         self.spin = round(random()) - 0.5
#
#     def __repr__(self):
#         return repr(f"This is a particle with a position of {self.x}, a momentum of {self.p}, andpin of {self.spin}")

# ========================================================

# EXERCISE 4


from random import random
from random import randint


class QuantumParticle:
    def __init__(self,x ,p):
        # self.x = randint(0, 50)
        self.x = x
        # self.p = random() * 50
        self.p = p
        self.spin = round(random()) - 0.5
        self.entangled = False
        self.entangled_with = None

    def measurePosition(self):
        self.x = randint(0, 50)
        self.p = random() * 50
        print("Quantum Interference")

    def measureMomentum(self):
        self.p = random() * 50
        self.x = randint(0, 50)
        print("Quantum Interference")

    def measureSpin(self):
        self.spin = round(random()) - 0.5
        if self.entangled:
            self.entangled_with.spin = self.spin * (-1)
            print("Spooky action at a distance!")

    def entangle(self, particle):
        self.entangled = True
        self.entangled_with = particle
        particle.entangled = True
        particle.entangled_with = self

    def __repr__(self):
        return repr(f"This is a particle with a position of {self.x}, a momentum of {self.p}, and spin of {self.spin}")


p1 = QuantumParticle(x=1, p=5.0)
p2 = QuantumParticle(x=2, p=5.0)
p1.entangle(p2)
p1.measureSpin()