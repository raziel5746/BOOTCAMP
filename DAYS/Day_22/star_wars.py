import random

class ForceWielder:
    def __init__(self):
        self.name = input("Choose a name: ")
        self.power = random.randrange(1, 16)
        self.wisdom = random.randrange(1, 16)
        self.average = 2 / (1/self.power + 1/self.wisdom)
        self.lightsaber_color = ''

    def train(self):
        pass

    def fight(self, enemy):
        print(f"{self.name} is fighting {enemy.name}!")
        if self.average > enemy.average:
            # self.wins = True
            enemy.loses = 1
            print(f"{self.name} defeated {enemy.name} with his amazing {self.lightsaber_color} lightsaber.")
            self.train()
        else:
            # self.loses = True
            # enemy.wins = True
            print(f"{self.name} was defeated, but quickly recovers! {enemy.name} prepares his {enemy.lightsaber_color} lightsaber for the next fight.")
            self.train()
            enemy.train()

    def is_jedi(self):
        pass


class Jedi(ForceWielder):
    def __init__(self):
        super().__init__()
        self.lightsaber_color = 'green'
        self.wisdom += 10
        if self.wisdom > self.power:
            self.lightsaber_color = 'green'
        elif self.wisdom < self.power:
            self.lightsaber_color = 'red'
        else:
            self.lightsaber_color = 'purple'
        self.average = 2 / (1/self.power + 1/self.wisdom)
        self.wins = False
        self.loses = 0

    def train(self):
        self.wisdom += random.randrange(10, 21)
        self.power += random.randrange(5, 16)
        self.average = 2 / (1/self.power + 1/self.wisdom)
        print(f"{self.name} trained.")
    
    def is_jedi(self):
        return True


class Sith(ForceWielder):
    def __init__(self):
        super().__init__()
        self.name = f"Darth {self.name}"
        self.lightsaber_color = 'red'
        self.power += 10
        self.wins = False
        self.loses = 0
    
    def train(self):
        self.power += random.randrange(10, 21)
        self.wisdom += random.randrange(5, 15)
        self.average = 2 / (1/self.power + 1/self.wisdom)
        print(f"{self.name} trained.")

    def is_jedi(self):
        return False