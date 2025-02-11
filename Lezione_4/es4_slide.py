def check_each(numbers:list):
    for i in numbers:
        if i > 5:
            print("bigger")
        elif i < 5:
            print("smaller")
        else:
            print("equal")

x:list = [1, 2, 3, 4, 5, 6]

check_each(x)