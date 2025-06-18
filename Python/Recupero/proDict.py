def proDict():
    d:dict[tuple, int] = {}
    x:int = 0
    y:int = 0
    somma:int = 0

    for i in range(101):
        for j in range(2, 89, 2):
            x = i
            y = j

            d[(x, y)] = x * y

    for i in d.values():
        somma += i

    return somma

print(proDict())