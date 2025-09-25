n_tutor:int = 10
attesa:int = 10
studente:str = input("inserisci il nome dello studente: ")

while True:
    if n_tutor == 0 and attesa > 50:
        break
    else:
        if n_tutor > 0:
            n_tutor -= 1
            print("tutor assegnato con successo")
        else:
            attesa += 1
            print("stedente in attesa")

        studente = input("inserisci il nome dello studente: ")

