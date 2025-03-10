#5-11

number_list:list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for numbers in number_list:
    if numbers == 1:
        print(f'{numbers}st')
    elif numbers == 2:
        print(f'{numbers}nd')
    elif numbers == 3:
        print(f'{numbers}rd')
    else:
        print(f'{numbers}th')