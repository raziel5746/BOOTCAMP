## EXERCISE 01
import datetime
today = datetime.date.today()

def get_age(year, month, day):
    birth_date = datetime.date(year, month, day)
    age = int((today - birth_date).days / 365)
    return age

def can_retire(gender, ):



get_age(1986, 6, 10)