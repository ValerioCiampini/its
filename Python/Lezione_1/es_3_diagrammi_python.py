somma:int = 0

for i in range(5):
    n:int = int(input("inserisci un numero: "))
    if n > 0:
        somma += n
    
print(somma)
