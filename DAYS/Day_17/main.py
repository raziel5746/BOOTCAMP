## Exercises


 ## 01

# height = int(input("Hi, how tall are you? "))

# if height < 35:
#     print("Sorry, you are not tall enough.")
# else:
#     print("Welcome! Have a nice ride.")



 ## 02

# num = int(input("Enter an integer: "))

# if num % 2 == 0:
#     print("The entered number is even")
# else:
#     print("The entered number is odd")


 
 ## 03 Doesn't make sense


 ## 04

# list = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]
# print(f"Original list: {list}")

#-----------
# listSorted = sorted(list, reverse = True)

# print(f"From greatest to lowest: {listSorted}")

#-----------
# listSum = sum(list)
# print(f"The sum of all items: {listSum}")

#-----------
# list2 = [list[0], list[-1]]  # This way

# list2.append(list[0])      # Or th
# list2.append(list[-1])     #      is way
# print(list2)

#-----------
# list50 = []
# for numbers in list:
#     if numbers > 50:
#         list50.append(numbers)

# print(list50)

#-----------
# list10 = []
# for numbers in list:
#     if numbers <10:
#         list10.append(numbers)

# print(list10)

#-----------
# listSq = []
# for number in list:
#     listSq.append(number ** 2)

# print(listSq)

#-----------
# list2 = [3, 21, 76, 53, 9, -82, -3, 49, 1, 76]

# listClean = list(set(list2))
# listCleanLen = len(listClean)

# print(f"Here is the list without duplicates: {listClean}. This list has {listCleanLen} items")

#-----------
# list3 = [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]

# listAvrg = sum(list3) / len(list3)

# print(f"The average of all the numbers of the list is {listAvrg}")

#-----------
# list3 = [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]

# maxNum = max(list3)
# minNum = min(list3)

# print(f"The maximum number of the list is {maxNum}, and the minimum is {minNum}.")

#-----------
listCustom = []

i = 0
while i < 10:
    listCustom.append(int(input("Enter an integer between -100 and 100: ")))
    i+=1

