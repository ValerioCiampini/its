nome:str = input("inserisci il nome: ")
vendite:int = int(input("inserisci la vendita: "))
max_nome = nome
max = vendite
min_nome = nome
min = vendite

for i in range(20):
    new_nome:str = input("inserisci il nuovo nome: ")
    new_vendite:int = int(input("inserisci la nuva vendita: "))
    if new_vendite > max:
        max_nome = new_nome
        max = new_vendite
    elif new_vendite < min:
        min_nome = new_nome
        min = new_vendite

print(max, max_nome)
print(min, min_nome)
