i:int = 0
pari:int = 0
dispari:int = 0
while i < 10:
    n:int = int(input("inserisci un numero: "))
    if n % 2 == 0:
        pari += 1
    else:
        dispari += 1
    i += 1

print(pari, dispari)