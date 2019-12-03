import random
from time import sleep
from os import system

cells = []
width = int(input("Enter an integer to set the size of the universe: "))
grid_measures = [width, width]

def gen_grid():
    for i in range(width):
        cells.append([])
        for j in range(width):
            cells[i].append([])


class Cell:
    def __init__(self, i, j):
        self.is_alive = round(random.random())
        self.live_neighbours = 0
        self.i = i
        self.j = j

    def check_neighbours(self):
        i = self.i
        j = self.j
        if i > 0:
            if j > 0:
                if cells[i-1][j-1].is_alive: self.live_neighbours += 1
            if cells[i-1][j].is_alive:
                self.live_neighbours += 1
            if j < width - 1:
                if cells[i-1][j+1].is_alive:
                    self.live_neighbours += 1
        if j > 0:
            if cells[i][j-1].is_alive:
                self.live_neighbours += 1
        if j < width - 1:
            if cells[i][j+1].is_alive:
                self.live_neighbours += 1
        if i < width - 1 and j > 0:
            if cells[i+1][j-1].is_alive:
                self.live_neighbours += 1
        if i < width - 1:
            if cells[i+1][j].is_alive:
                self.live_neighbours += 1
        if i < width - 1 and j < width - 1:
            if cells[i+1][j+1].is_alive:
                self.live_neighbours += 1

    def next_gen(self):
        if self.is_alive and self.live_neighbours < 2:
            self.is_alive = False
        elif self.is_alive and self.live_neighbours > 3:
            self.is_alive = False
        elif self.is_alive and (2 <= self.live_neighbours <= 3):
            self.is_alive = True
        elif not self.is_alive and self.live_neighbours == 3:
            self.is_alive = True
        self.live_neighbours = 0

    def __repr__(self):
        if self.is_alive:
            return ' o'
        else:
            return '  '

string = "\x1b[0;31;41m" + "this" + "\x1b[0m"

def populate_grid():
    for i in range(width):
        for j in range(width):
            cells[i][j] = Cell(i, j)

def print_grid():
    print("\n\n")
    display = ""
    for row in cells:
        for cell in row:
            display += cell.__repr__()
        display += "\n"
    print(display)


if __name__ == "__main__":
    gen_grid()
    populate_grid()
    print_grid()
    
    for i in range(1000):
        for row in cells:
            for cell in row:
                cell.check_neighbours()
        for row in cells:
            for cell in row:
                cell.next_gen()
        system('clear')
        print_grid()
        sleep(0.04166)
