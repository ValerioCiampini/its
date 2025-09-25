n:int = int(input("inserisci un numero intero: "))
while True:
    if n % 1 == 0:
        break
    else:
        n:int = int(input("inserisci un numero intero positivo: "))

if n % 2 == 0 and n > 10:
    print("numero valido")
else:
    print("numero non valido")