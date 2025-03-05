def make_album(name:str, album_title:str, number_songs:int = None):
    album:dict = {}
    album["name artist"] = name
    album["album title"] = album_title
    if number_songs != None:
        album["number of songs"] = number_songs
    return album

print(make_album("a", "b"))
print(make_album("c", "d"))
print(make_album("e", "f"))
print(make_album("g", "h", 6))