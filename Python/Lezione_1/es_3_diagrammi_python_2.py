max_posti = 100
nome_corso:str = input("inserisci il nome del corso: ")

while True:
    opzione:str = input("inserisci un opzione tra:\n'iscrivi' per iscriverti ad un corso\n'annulla' per annullare l'iscrizione ad un corso\n'visualizza' per vedere i posti liberi e occupati\n'elimina' per cambiare corso\n'esci' per uscire: ")
    match opzione:
        case "iscrivi":
            if max_posti > 0:
                max_posti -= 1
                print("iscrizione effettuata")
            else:
                print("non ci sono posti disponibili")
        case "annulla":
            if max_posti < 100:
                max_posti += 1
                print("iscrizione annullata")
            else:
                print("tutti i posti sono già disponibili")
        case "visualizza":
            print(max_posti, 100 - max_posti)
        case "elimina":
            nome_corso = input("inserisci nome corso: ")
            max_posti = 100
        case "esci":
            break
        case _:
            print("inserisci un comando valido")

