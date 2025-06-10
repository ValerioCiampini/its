def ricerca_binaria(lista:list[int], numero:int):
    inizio = 0
    fine = len(lista) - 1
    trovato = False
    
    while inizio <= fine and not trovato:
        meta = (inizio + fine) // 2
        if lista[meta] == numero:
            trovato = True
        else:
            if numero < lista[meta]:
                fine = meta - 1
            else: 
                inizio = meta + 1

    return trovato

print(ricerca_binaria([1, 2, 3, 4, 5, 6, 7, 8], 7))
