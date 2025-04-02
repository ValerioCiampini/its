a:int = int(input("inserisci un numero intero positivo: "))
b:int = int(input("inserisci un numero intero positivo: "))

if a < b:
    if a > 0 and b > 0:
        if a % 1 == 0 and b % 1 == 0:
            somma:int = 0
            i:int = a
            while i <= b:
                somma += i
                i += 1
            
            print(somma)
        else:
            print("a e b devono esere interi")
    else:
        print("a e b devono essere positivi")
else:
    print("a deve essere minore di b")