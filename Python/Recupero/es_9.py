from string import ascii_lowercase

def caesar_cypher_encrypt(s:str, key:int):
    alfabeto_maiuscolo:list[str] = []
    for i in ascii_lowercase:
        alfabeto_maiuscolo.append(i.upper())
        
    
