max_posti:int = int(input("Inserisci numero massimo posti: "))
posti_disp:int = max_posti

while True:
    opzione:str = str(input("Inserisci una delle seguenti opzioni \"ingresso\" \"uscita\" \"stato\" \"esci\": "))
    if opzione == "ingresso":
        if posti_disp > 0:
            posti_disp -= 1
        else: 
            print("non ci sono posti diponibili")
    elif opzione == "uscita":
        if posti_disp < max_posti:
            posti_disp += 1
        else:
            print("non ci sono veicoli registrati")
    elif opzione == "stato":
        print(f"i posti disponibili sono: {posti_disp}. i posti occupati sono {max_posti - posti_disp}")
    elif opzione == "esci":
        break
    else:
        print("azione non disponibile")
