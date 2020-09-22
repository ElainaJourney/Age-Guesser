from datetime import datetime

birth_year = int(input("what year were you born?"))
current_year = int(datetime.now().year)
age = current_year - birth_year

print(f'you are either {age -1} or {age} years old')