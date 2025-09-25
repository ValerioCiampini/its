dispari:int = 0
pari:int = 0
positivi:int = 0
negativi:int = 0

for i in range(10):
    n:int = int(input("inserisci un valore intero: "))

    while True:
        if n != 0:
            break
        else:
            print("il valore non deve essere 0")
            n:int = int(input("inserisci un valore intero: "))

    if n > 0:
        positivi += 1
        if n % 2 == 0 and n > 20:
            pari += 1
    else:
        negativi += 1
        if n % 2 != 0 and n < -10:
            dispari += 1

print(pari, dispari, negativi, positivi)
