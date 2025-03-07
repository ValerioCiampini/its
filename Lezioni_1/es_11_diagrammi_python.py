liberi:int = 20
while True:
    opzione:str = input("inserisci prenota per prenotare un posto\ninserisci libera per liberare un posto\ninserisci visualizza per vedere il numero dei posti liberi e occupati\ninserisci esci per uscire: ")
    match opzione:
        case "prenota":
            if liberi > 0:
                liberi -= 1
                print("posto prenotato")
            else:
                print("non ci sono posti disponibili")
        case "libera":
            if liberi < 20:
                liberi += 1
                print("posto liberato")
            else:
                print("tutti i posti sono già liberi")
        case "visualizza":
            print(liberi, 20 - liberi)
        case "esci":
            break
        case _:
            print("opzione non disponibile")
