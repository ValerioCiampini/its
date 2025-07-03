def printListBackward(lista):
    if not lista:
        print(" ")
    else:
        print(lista[-1])
        printListBackward(lista[:-1])

printListBackward([1, 2, 3, 4, 5])