a:float = float(input("inserisci il valore dell'ipotenusa: "))
b:float = float(input("inserisci il valor del cateto: "))

if a > b:
    c = (a**2 - b**2)**(1/2)
    print(c)
else:
    print("Errore")