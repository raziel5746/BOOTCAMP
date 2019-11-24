# user_profile = {
#     'username': "John",
#     'age': "30",
#     'weapons': ['shotgun', 'knife', 'spoon'],
#     'is_active': "True",
#     'clan': "The Cleaners",
#     'is_banned': False
#     }


# user_profile['is_banned'] = True
# print(user_profile['username'] + " banned status: " + str(user_profile.get('is_banned')))

# new_user = user_profile.copy()

# new_user.update(username='Peter', age=36)
# print(new_user)
# print(user_profile)

##==============================================================



def some_function(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        print("Args: " + str(args))
        print("Items: " + str(items))
        total += items
    return sum(args) + total

print(some_function(1,2,3,4, num1 = 5, num2 = 6))