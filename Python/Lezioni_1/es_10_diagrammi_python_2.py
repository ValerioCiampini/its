età:int = int(input("inserisci età: "))

match età:
    case età if età >= 18 and età <= 65:
        print("puoi partecipare all'attività")
    case età if età < 18:
        print("non puoi partecipare all'attivita perchè troppo piccolo")
    case _:
        print("non puoi partecipare all'attività perchè troppo grande")
