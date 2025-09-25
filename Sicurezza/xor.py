frase = "Nel mezzo del cammin di nostra vita"
valore = 57
lista1 = []
lista2 = []
lista3 = []

for i in range(len(frase)):
    lista1.append(ord(frase[i]))
    lista2.append(lista1[i] ^ valore)

print(lista2)


for i in lista2:
    lista3.append(chr(i ^ 57))

print("".join(lista3))
