magicians = ["David Copperfield", "Rene Lavand", "Penn and Teller", "Henry Evans", "Chris Angel", "David Blaine"]

def show_magicians():
    for i in range(len(magicians)):
        print(magicians[i])

def make_great(list):
    for i in range(len(magicians)):
        magicians[i] = "The Great " + magicians[i]



make_great(magicians)
show_magicians()