#5-6

age:int = int(input('My age is:'))
if age < 2:
    print('Newborn')
elif age >= 2 and age < 4:
    print('Toddler')
elif age >= 4 and age < 13:
    print('kid')
elif age >= 13 and age < 20:
    print('Teenager')
elif age >= 20 and age < 65:
    print('Adult')
elif age >= 65:
    print('Elder')