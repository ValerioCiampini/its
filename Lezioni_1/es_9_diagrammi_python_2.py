n:int = int(input("inserisci un numero intero positivo: "))

if n > 0:
    while True:
        if n % 1 == 0:
            break
        else:
            print("n deve essere intero")
            n:int = int(input("inserisci un numero intero positivo: "))
    
    i:int = 0

    for j in range(10):
        x:int = int(input("inserisci un numero: "))
        if x % n == 0:
            i += 1
    
    print(i)

else:
    print("n deve essere positivo")