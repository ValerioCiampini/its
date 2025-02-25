oggetti:list = []

while len(oggetti) < 3:
    oggetto:str = str(input("inserire 3 oggetti inerenti tra loro: "))
    oggetti.append(oggetto)

match oggetti:
    case ["penna", "matita", "quaderno"]:
        print("Materiale scolastico")
    case ["pane", "latte", "uova"]:
        print("prodotti alimentari")
    case ["sedia", "tavolo", "armadio"]:
        print("mobili")
    case ["telefono", "computer", "tablet"]:
        print("dispositivi elettronici")
    case _:
        print("categoria non riconosciuta")

