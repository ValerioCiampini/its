soglia:int = int(input("inserisci la soglia: "))
i:int = 0
numeri:list[int] = []
while i < 7:
    n:int = int(input("inserisci un numero: "))
    if n > soglia:
        numeri.append(n)
    i += 1

print(*numeri)