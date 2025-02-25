nome:str = str(input("inserisci il tuo nome: "))
genere:str = str(input("inserisci il tuo genere (scrivendo m in caso di maschio o f in caso di femmina): "))

match genere:
    case "m":
        print(f"Nome: {nome} \nGenere: Maschio")
    case "f":
        print(f"Nome: {nome} \nGenere: Femmina")
    case _:
        print("Errore. non è possibile generare un documento di identità.")