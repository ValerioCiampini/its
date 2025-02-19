#5-8

usernames:list = ['Frank', 'Josie', 'Luke', 'Mark', 'admin']

for people in usernames:
    if people == 'admin':
        print(f'Hello admin, would you like to see a status report?')
    elif len(usernames) == 0:
        print('We need more people')     #5-9
    else:
        print(f'Hello {people}, thank you for logging in!')