import random

class BankAccount:
    def __init__(self, owner_name):
        self.owner = owner_name
        self.balance = random.randint(0, 50000)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'You have deposited {amount} dollars on your account.\nYour current balance is {self.balance} dollars.')
        else:
            print('The amount entered is invalid.')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'You withdrew {amount} dollars. Your current balance is {self.balance}.')
        else:
            print(f'Your balance ({self.balance}) is not enough for withdrawing {amount} dollars.')


class Owner(BankAccount):
    def __init__(self, owner_name):
        super().__init__(owner_name)

        self.cc = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))

        self.password = "abc"

    def check_owner_info(self, cc, password):
        if cc == self.cc and password == self.password:
            
