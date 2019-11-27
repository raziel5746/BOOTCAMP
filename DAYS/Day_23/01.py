# def decorator(func):
#     def wrapper():
#         do
#         func()
#         do
#     return wrapper
# ====================================
# def play(func):
#     def wrapper():
#         print("Playing")
#         func()
#         print("Pausing")
#     return wrapper


# @play
# def sing_the_beatles():
#     print("The gool on the hill...")


# if __name__ == "__main__":
#     sing_the_beatles()

# =====================================
# from datetime import datetime

# def calctime(func):
#     def wrapper(*args):
#         start = datetime.now()
#         output = func(*args)
#         end = datetime.now()
#         secs = (end - start).seconds
#         microsecs = (end - start).microseconds
#         print(f"Execution time: {secs}s {microsecs}us")
#         return output
#     return wrapper

# @calctime
# def compute():
#     return 2 ** 1000

# @calctime
# def power_2(power):
#     return 2 ** power

# if __name__ == "__main__":
#     # compute()
#     print(power_2(100))

# ======================================================

# SUPER()

class Book:
    def __init__(self, title, author, publication_date, price, is_good):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.price = price
    
    def present(self):
        print(f'Title: {self.title}')


class Fiction(Book):
    def __init__(self,title, author, publication_date, price, is_good):
        super().__init__(title, author, publication_date, price, is_good)
        self.genre = 'Fiction'
        self.is_good = is_good
        if self.is_good == True:
            self.bored = False
            print("This is a good book.")
        else:
            self.bored = True
            print("This book is boring")

    
if __name__ == "__main__":
    # foundation = Fiction('Foundation', 'Asimov', 1951, '$5', True)
    # foundation.present()
    # print(foundation.price)
    # print(foundation.is_good)
    boring_book = Fiction('boring title', 'boring author', 'some date', '$500', False)
    print(boring_book)