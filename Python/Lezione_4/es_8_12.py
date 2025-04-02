def sandwich(lista1:list):
    i:int = 0
    lista2:list = []
    while i < len(lista1):
        scelta = input(f"vuoi inserire {lista1[i]} nel panino? ")
        if scelta == "si":
            lista2.append(lista1[i])
            i += 1
        elif scelta == "no":
            i += 1
            continue
        else: 
            print("comando non riconosciuto")
            continue


    return lista2

ingredienti:list = ["pommodoro", "tonno", "prosciutto", "insalata"]

print(sandwich(ingredienti))

