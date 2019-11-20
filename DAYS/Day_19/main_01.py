## EXERCISES

## 01

# import random

# def get_random_temp(min, max):
#     return random.randint(min, max)

# print(get_random_temp(-10, 40))
##=========================================



## 02

# import random

# def get_random_temp(min, max):
#     return random.randint(min, max)

# def main():
#     myTemp = get_random_temp(-10, 40)
#     print(f"I predict that the temperature tomorrow will be {myTemp}°C.")

# main()
##=========================================



## 03

# import random

# def get_random_temp(min, max):
#     return random.randint(min, max)

# def main():
#     myTemp = get_random_temp(-10, 40)
#     print(f"I predict that the temperature today will be {myTemp}°C.")
#     if myTemp < 0:
#         print("Wow, it's literally freezing outside. Stay home dude.")
#         return
#     if 0 <= myTemp < 16:
#         print("Hey, it's pretty chilly, get your warmest coat.")
#         return
#     if 16 <= myTemp < 23:
#         print("It's cold outside, get your coat")
#         return
#     if 24 <= myTemp < 32:
#         print("Nice weather. Enjoy the day.")
#         return
#     if 32 <= myTemp < 40:
#         print("It's so hoooot today. Go to the beach, skip work.")
#         return
# main()
##=========================================



## 04

# import random

# def get_random_temp(season):
#     if season == "winter":
#         min = -10
#         max = 16
#         print("a" + season)
#     if season == "spring":
#         min = 16
#         max = 31
#         print("b" + season)
#     if season == "summer":
#         min = 24
#         max = 40
#         print("c" + season)
#     if season == "autumn" or season == "fall":
#         min = 5
#         max = 20
#         print("d" + season)
#     return round(random.uniform(min, max), 1)

# def main():
#     season = input("Enter a season: ")
#     myTemp = get_random_temp(season)
#     print(f"I predict that the temperature today will be {myTemp}°C.")
#     if myTemp < 0:
#         print("Wow, it's literally freezing outside. Stay home dude.")
#         return
#     if 0 <= myTemp < 16:
#         print("Hey, it's pretty chilly, get your warmest coat.")
#         return
#     if 16 <= myTemp < 23:
#         print("It's cold outside, get your coat")
#         return
#     if 24 <= myTemp < 32:
#         print("Nice weather. Enjoy the day.")
#         return
#     if 32 <= myTemp < 40:
#         print("It's so hoooot today. Go to the beach, skip work.")
#         return
# main()
##=========================================



## 05

import random

month = 0

def get_random_temp(season):
    if season == "winter":
        min = -10
        max = 16
    if season == "spring":
        min = 16
        max = 31
    if season == "summer":
        min = 24
        max = 40
    if season == "autumn":
        min = 5
        max = 20
    return round(random.uniform(min, max), 1)

def get_season(month):
    if 1 <= month <= 3:
        return "winter"
    if 4 <= month <= 6:
        return "spring"
    if 7 <= month <= 9:
        return "summer"
    if 10 <= month <= 12:
        return "autumn"

def main():
    month = int(input("Enter a month as en integer (1-12): "))
    myTemp = get_random_temp(get_season(month))
    print(f"I predict that the temperature today will be {myTemp}°C.")
    if myTemp < 0:
        print("Wow, it's literally freezing outside. Stay home dude.")
        return
    if 0 <= myTemp < 16:
        print("Hey, it's pretty chilly, get your warmest coat.")
        return
    if 16 <= myTemp < 23:
        print("It's cold outside, get your coat")
        return
    if 24 <= myTemp < 32:
        print("Nice weather. Enjoy the day.")
        return
    if 32 <= myTemp < 40:
        print("It's so hoooot today. Go to the beach, skip work.")
        return

main()