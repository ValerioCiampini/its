n:int = int(input("inserisci un numero intero e positivo: "))

if n > 0:
    somma:int = 0
    
    for i in range(n + 1):
        somma += i*i

    print(somma)

else:
    print("Errore. devi inserire un numero intero positivo")