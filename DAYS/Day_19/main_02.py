import random
import math

def throw_2_dice():
    die_1 = int(math.ceil(random.random() * 6))
    die_2 = int(math.ceil(random.random() * 6))
    return (die_1, die_2)

def throw_until_doubles():
    dice = throw_2_dice()
    throws = 1
    while dice[0] != dice[1]:
        dice = throw_2_dice()
        throws += 1
        print(dice[0], dice[1])
    else:
        print(dice[0], dice[1])
        print("EQUALLLLLLLLLLLLLLLLLLLLLLLL")
        return throws

def main():
    throws_collection = []
    for i in range(100):
        throws_collection.append(throw_until_doubles())
    total_throws = sum(throws_collection)
    average_throws = round(total_throws / len(throws_collection), 2)
    print(f"In order to reach 100 doubles, the dice were thrown a total of {total_throws} times")
    print(f"And the average amount of throws was {average_throws}")

main()