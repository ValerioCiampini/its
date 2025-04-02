fattoriale:int = 1
i:int = 1
while True:
    n:int = int(input("inserisci un numero positivo: "))
    if n > 0:
        break
    else: 
        print("devi in serire un numero intero positivo")

while i <= n:
    fattoriale *= i
    i += 1

print(fattoriale)