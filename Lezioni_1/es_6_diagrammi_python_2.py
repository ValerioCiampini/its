x:int = int(input("inserisci un numero positivo: "))
somma_p:int = 0
somma_d:int = 0

if x > 0:
    for i in range(10):
        n:int = int(input("inserisci un numero: "))
        if n % 2 == 0:
            if n > x / 2:
                somma_p += n
        else:
            if n < x:
                somma_d += n

print(somma_d, somma_p)