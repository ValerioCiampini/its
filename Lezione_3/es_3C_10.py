giorno:int = int(input("inserisci un giorno: "))
mese:int = int(input("inseridci un mese: "))

festa:tuple = (giorno, mese)

match festa:
    case festa if giorno == 1 and mese == 1:
        print(f"Il {giorno}/{mese} è Capodanno")
    case festa if giorno == 14 and mese == 2:
        print(f"Il {giorno}/{mese} è San Valentino")
    case festa if giorno == 2 and mese == 6:
        print(f"Il {giorno}/{mese} è la festa delle Repubblica")
    case festa if giorno == 15 and mese == 8:
        print(f"Il {giorno}/{mese} è Ferragosto")
    case festa if giorno == 31 and mese == 10:
        print(f"Il {giorno}/{mese} è Halloween")
    case festa if giorno == 25 and mese == 12:
        print(f"Il {giorno}/{mese} è Natale")
    case _:
        print("Nessuna festività prevista in questa data")