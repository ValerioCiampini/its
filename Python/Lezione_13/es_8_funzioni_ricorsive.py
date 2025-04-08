def vowelsCounter(stringa:str) -> int:
    if not stringa:
        return 0 
    
    if stringa[0].lower() in ["a", "e", "i", "o", "u"]:
        return 1 + vowelsCounter(stringa[1:])
    else:
        return 0 + vowelsCounter(stringa[1:])

print(vowelsCounter("Ciao"))