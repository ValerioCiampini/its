def make_album():
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




