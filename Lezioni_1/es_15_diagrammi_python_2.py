n:int = int(input("inserisci un valore intero n: "))

if n > 0 and n <= 100:
    somma:int = 0

    for i in range(n + 1):
        if i % 2 == 0:
            somma += i
    
    print(somma)

else:
    if n == 0 or n < 0:
        print("errore")
    else:
        somma:int = 0

        for i in range(n + 1):
            if i % 2 != 0:
                somma += i
        
        print(somma)