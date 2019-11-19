import datetime

today = datetime.date.today()
birthdate_input = input("Enter your birthdate in the following format: DD/MM/YYYY: ")
day = int(birthdate_input[:2])
month = int(birthdate_input[3:5])
year = int(birthdate_input[6:])
birthdate = datetime.date(year, month, day)
age = int((today - birthdate).days / 365)
last_digit = str(age)[-1]
candles = "i" * int(last_digit)
topping = candles.center(11)

if int(last_digit) == 0:
    topping = "iiiii iiiii"
else:
    first_i = topping.index("i")
    if len(candles) % 2 == 0:
        topping = topping[0:(first_i - 1)] + "i" + topping[first_i:5] + " " + topping[6:]

topping = topping.replace(" ", "_")

cake = f'''
       {topping}
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
'''

print(cake)