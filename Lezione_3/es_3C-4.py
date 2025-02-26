animale:str = str(input("inserisci il nome di un amìnimale: "))

match animale:
    case animale if animale in ["cane", "gatto", "cavallo", "elefante", "leone"]:
        print(f"{animale} è un mammifero")
    case animale if animale in ["serpente", "lucertola", "tartaruga", "coccodrillo"]:
        print(f"{animale} è un rettile")
    case animale if animale in ["aquila", "pappagallo", "gufo", "falco"]:
        print(f"{animale} è un uccello")
    case animale if animale in ["squalo", "trota", "salmone" ,"carpa"]:
        print(f"{animale} è un Pesce")
    case _:
        print(f"Non so dire in quale categoria classificare l'animale {animale}!")