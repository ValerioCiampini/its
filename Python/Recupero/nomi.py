def nomi():
    l:list = []
    massimo:int
    nomemax:str = ""
    while True:
        nome = input("inserisci un nome: ")
        nome = nome.replace(" ", "")
        
        if nome in l or len(l) == 31:
            break
        
        if len(nome) > 20 or nome == "":
            continue

        l.append(nome)

        if len(nome) > len(nomemax):
            nomemax = nome
            massimo = len(nome)

    print(f"hai iserito {len(l)} nomi")
    print(f"il più lungo è {nomemax} con {massimo}")

nomi()
        

