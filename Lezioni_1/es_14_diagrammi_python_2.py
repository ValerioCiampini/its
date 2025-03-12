punteggio:int = 0
somma:int = 0

while punteggio < 100:
    d1:int = int(input("inserisci il punteggio del primo dado: "))
    d2:int = int(input("inserisci il punteggio del secondp dado: "))

    while True:
        if (d1 > 0 and d1 <= 6) and (d2 > 0 and d2 <= 6):
            break
        else: 
            print("dado non valido")
            d1:int = int(input("inserisci il punteggio del primo dado: "))
            d2:int = int(input("inserisci il punteggio del secondp dado: "))
    
    somma = d1 + d2
    
    if d1 % 2 == 0 and d2 % 2 == 0 and somma > 8:
        punteggio = 100
    elif d1 == 6 or d2 == 6 or somma == 7:
        punteggio += 10
    else: 
        punteggio = 0
        print("sconfitta")
        break

if punteggio >= 100:
    print(f"vittoria. punteggio: {punteggio}")

                