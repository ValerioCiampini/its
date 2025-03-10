def show_messages(lista1:list):    #8-9
    for i in lista1:
        print(i)

messaggi:list = ["ciao", "come va?", "chi sei?", "ci sei?"]
if __name__ == "__main__":
    show_messages(messaggi)

#ho seguito le linee guida

def make_album():   #8-8
    album:dict = {}
    while True:
        scegli:str = input("inserire continua per inserire un nuvo album o esci per uscire: ")
        if scegli == "esci":
            break
        elif scegli == "continua":
            name:str = input("inserisci il nome dell'artista: ")
            album_title:str = input("inserisci il titolo dell'artista: ")
            album[name] = album_title
        else:
            print("opzione non disponibile")
            continue
    
    return print(album)

make_album()

#ho seguito le linee guida

messaggi:list = ["ciao", "come va?", "chi sei?", "ci sei?"]     #8-10

def show_messages(lista1:list):
    for i in lista1:
        print(i)

def send_messages(lista1:list):
    lista2:list = []
    for i in lista1:
        print(i)
        lista2.append(i)
    return lista2, lista1

print(send_messages(messaggi))


#ho seguito le linee guida