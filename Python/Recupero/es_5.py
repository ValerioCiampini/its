def moltiplica(lista:list[int], treshold:int):
    prodotto:float = 1

    for i in lista:
        if i < treshold:
            prodotto *= i

    return prodotto

print(moltiplica([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))