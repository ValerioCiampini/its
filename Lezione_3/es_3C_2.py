voto:int = int(input("inserire voto esame (da 66 a 110): "))

match voto:
    case voto if voto >= 106 and voto <= 110:
        print("Output: GPA 4.0")
    case voto if voto >= 101 and voto <= 105:
        print("Output: GPA 3.7")
    case voto if voto >= 96 and voto <= 100:
        print("Output: GPA 3.3")
    case voto if voto >= 91 and voto <= 95:
        print("Output: GPA 3.0")
    case voto if voto >= 86 and voto <= 90:
        print("Output: GPA 2.7")
    case voto if voto >= 81 and voto <= 85:
        print("Output: GPA 2.3")
    case voto if voto >= 76 and voto <= 80:
        print("Output: GPA 2.0")
    case voto if voto >= 70 and voto <= 76:
        print("Output: GPA 1.7")
    case voto if voto >= 69 and voto <= 66:
        print("Output: GPA 1.0")
    case _:
        print("voto non valido")