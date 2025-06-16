def sequenza_interi(x:int):
    lista_sequenze:list[int] = []
    occ:int = 0
    pos:int
    somma:int = 0
    unica:bool = False

    while True:
        y = int(input("inserisci un intero positivo: "))
        if y < 0 and y.is_integer() == False:
            continue
        else:
            lista_sequenze.append(y)
            if y == 0:
                break

    for i in range(len(lista_sequenze)):
        if lista_sequenze[i] != x:
            somma += lista_sequenze[i]
        if lista_sequenze[i] == x:
            occ += 1
            if occ == 1 and unica == False:
                pos = i
                unica = True

    return lista_sequenze, occ, pos, somma

z = sequenza_interi(4)
print(z)
                

