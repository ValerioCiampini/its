somma:int = 0
i:int = 0
media:float = 0

while True:
    scelta:str = input("inserisci si o no per inseire il voto o no: ")
    match scelta:
        case "si":
            while True:
                voto:int = int(input("inserisci voto: "))
                if voto > 0:
                    somma += voto
                    i += 1
                    break
                else:
                    print("errore")
        case "no":
            if i > 0:
                media = somma / i
                print("la media è ", media)
                break
            else:
                print("nessun voto inserito")
                break
        case _:
            print("devi inserire si o no")