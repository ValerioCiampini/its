n:int = int(input("inserisci un numero: "))
somma:int = 0
prodotto:int = 1

if n < 0:
    print("errore")
else:
    if n % 2 == 0:
        for j in range(0, n + 1, 4):
                somma += j
    else:
        for j in range(1, n + 1, 2):
            prodotto *= j
    
    print(somma, prodotto)
    






