# EXERCISE 1
felps_members = [
            {'name':'Michael', 'age':35, 'gender':'male', 'is_child':False},
            {'name':'Sarah', 'age':32, 'gender':'female', 'is_child':False},
            {'name':'Kevin', 'age':16, 'gender':'male', 'is_child':True}
            ]

felps_LN = 'Felps'

brian_felps = {'name':'Brian', 'age':0, 'gender':'male', 'is_child':True}

class Family:
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

    def born(self, **kwargs):
        new_child = {**kwargs}
        self.members.append(new_child)
        print(f"Congratulations!!! Welcome to the world, {['name']}!")

    def is_18(self, member):
        for family_member in self.members:
            if family_member.age >= 18:
                print("Already 18")
                return True
            else:
                print("Not 18 yet")
                return False