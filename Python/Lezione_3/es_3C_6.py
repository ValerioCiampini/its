animale:str = str(input("inserisci il nome di un animale: "))
habitat:str = str(input("inserisci il suo habitat(acqua, terra o aria): "))

match animale:
    case animale if animale in ["cane", "gatto", "cavallo", "elefante", "leone", "balena","delfino"]:
        print(f"{animale} è un mammifero")
        animal_type = "mammifero"
    case animale if animale in ["serpente", "lucertola", "tartaruga", "coccodrillo"]:
        print(f"{animale} è un rettile")
        animal_type = "rettile"
    case animale if animale in ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]:
        print(f"{animale} è un uccello")
        animal_type = "uccello"
    case animale if animale in ["squalo", "trota", "salmone" ,"carpa"]:
        print(f"{animale} è un Pesce")
        animal_type = "pesce"
    case _:
        print(f"Non so dire in quale categoria classificare l'animale {animale}!")
        animal_type = "unknown"

dict_animale:dict = {}
dict_animale["animale"] = animale
dict_animale["anymal_type"] = animal_type
dict_animale["habitat"] = habitat

match dict_animale:
    case dict_animale if dict_animale["animale"] in ["cane", "gatto", "cavallo", "elefante", "leone"]:
        match dict_animale:
            case dict_animale if dict_animale["habitat"] == "terra":
                print(f"{animale} è un {animal_type} che vive sulla terra")
            case _:
                print(f"non ho mai visto un {animale} in {habitat}")
    case dict_animale if dict_animale["animale"] in ["balena", "delfino"]:
        match dict_animale:
            case dict_animale if dict_animale["habitat"] == "acqua":
                print(f"{animale} è un {animal_type} che vive nell'acqua")
            case _:
                print(f"non ho mai visto un {animale} in {habitat}")
    case dict_animale if dict_animale["animale"] in ["serpente", "lucertola", "tartaruga", "coccodrillo"]:
        match dict_animale:
            case dict_animale if dict_animale["habitat"] == "terra" and dict_animale["animale"] in ["tartaruga", "coccodrillo", "serpente"] and dict_animale["habitat"] == "acqua":
                print(f"{animale} è un {animal_type} che può vivere sia in acqua che su terra")
            case dict_animale if dict_animale["habitat"] == "terra":
                print(f"{animale} è un {animal_type} che vive sulla terra")
            case _:
                print(f"non ho mai visto un {animale} in {habitat}")
    case dict_animale if dict_animale["animale"] in ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]:
        match dict_animale:
            case dict_animale if dict_animale["animale"] in ["anatra", "cigno"] and dict_animale["habitat"] in ["aria", "terra", "acqua"]:
                print(f"{animale} è un {animal_type} che vive in acqua, cielo e terra")
            case dict_animale if dict_animale["animale"] in ["gallina", "tacchino"] and dict_animale["habitat"] == "terra":
                print(f"{animale} è un {animal_type} che vive su terra")
            case dict_animale if dict_animale["animale"] in ["aquila", "pappagallo", "gufo", "falco"] and dict_animale["habitat"] == "aria":
                print(f"{animale} è un {animal_type} che vive in aria")
            case _:
                print(f"non ho mai visto un {animale} in {habitat}")
    case dict_animale if dict_animale["animale"] in ["squalo", "trota", "salmone" ,"carpa"]:
        match dict_animale:
            case dict_animale if dict_animale["habitat"] == "acqua":
                print(f"{animale} è un {animal_type} che vive in acqua")
            case _:
                print(f"non ho mai visto un {animale} in {habitat}")
    case _:
        print("Errore. Dati non validi")

