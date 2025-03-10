messaggi:list = ["ciao", "come va?", "chi sei?", "ci sei?"]

def show_messages(lista1:list):
    for i in lista1:
        print(i)

def send_messages(lista1:list):
    lista2:list = []
    for i in lista1:
        print(i)
        lista2.append(i)
    lista1.clear()
    return lista2, lista1

print(send_messages(messaggi))