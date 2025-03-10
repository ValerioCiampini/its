#5-10

current_users:list = ['John', 'Maria', 'Sam', 'Vincent', 'Caine']
new_users:list = ['Maria', 'Mark', 'Phenelophe', 'Mattew', 'JOHN']
users_old:list = list(map(str.upper, current_users))
for user in new_users:
    if user in users_old:
        print(f'The name {user} has already been taken')
    elif user != users_old:
        print(f'The name {user} is available')