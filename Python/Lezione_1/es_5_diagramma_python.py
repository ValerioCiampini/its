n:int = int(input("inserisci un numero: "))

if n < 2:
    print("il numero non è primo")
else:
    div = 2
    is_prime = True

    while div < n:
        if n % div == 0:
            is_prime = False
            break
        
        div += 1
    
    if is_prime:
        print("il numero è primo")
    else:
        print("il numero non è primo")