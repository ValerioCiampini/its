def convertitore(lista:list[tuple]):
    dict1:dict = {}

    for i, j in lista:
        if i in dict1:
            dict1[i] += j
        else:
            dict1[i] = j

    return dict1

print(convertitore([("a", 1), ("b", 2), ("a", 3)]))

