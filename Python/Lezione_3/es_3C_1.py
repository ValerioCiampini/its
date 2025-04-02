voto:int = int(input("inseisci il voto (da 1 a 10): "))

match voto:
    case 10:
        print("Output: Eccellente")
    case voto if voto == 9 or voto == 8:
        print("Output: Molto Buono")
    case voto if voto == 7 or voto == 6:
        print("Output: Sufficiente")
    case voto if voto == 5 or voto == 4:
        print("Output: Insufficiente")
    case voto if voto <= 3 or voto >= 1:
        print("Output: Gravemente insufficiente")
    case _:
        print("Output: voto non valido")
    