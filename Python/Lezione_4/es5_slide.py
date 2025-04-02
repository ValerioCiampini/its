def add_one(number:int):
    add = number + 1
    return add

def add_one_to_list(numbers:list):
    new_list = []
    for i in numbers:
        new_list.append(add_one(i))

    print(new_list)

x:list = [1, 2, 3, 4, 5, 6]

add_one_to_list(x)