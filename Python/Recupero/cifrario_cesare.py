from string import ascii_lowercase

def caesar_cypher_encrypt(s, key):
    cifrata:str = ""
    if key > 26:
        key -= 26
    for i in s: 
        j:int = 0
        if i.lower() in ascii_lowercase:
            while j < len(ascii_lowercase):
                if ascii_lowercase[j] == i.lower():
                    cifrata += ascii_lowercase[j + key]
                j += 1
        else:
            return "sono permesse solo lettere"

    return cifrata

def caesar_cypher_decrypt(s, key):
    decifrata:str = ""
    if key > 26:
        key -= 26
    for i in s: 
        j:int = 0
        if i.lower() in ascii_lowercase:
            while j < len(ascii_lowercase):
                if ascii_lowercase[j] == i.lower():
                    decifrata += ascii_lowercase[j - key]
                j += 1
        else:
            return "sono permesse solo lettere"

    return decifrata


e = caesar_cypher_encrypt("ciao", 28)

d = caesar_cypher_decrypt(e, 28)
print(d)



