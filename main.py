from datetime import datetime

current_year = int(datetime.now().year)
current_month = int(datetime.now().month)
year_or_age = input("Do you know the year or age?:  ")

if (year_or_age == "year" or year_or_age == "Year"):
    birth_year = int(input("What year were you born?:  "))
    age = current_year - birth_year
    print(f'You are either {age -1} or {age} years old')
if year_or_age == "age" or year_or_age == "Age":
    age = int(input("How old are you?:  "))
    birth_year = current_year - age
    print(f'You were born in {birth_year} or {birth_year + 1}.')
else:
    print("Try again")