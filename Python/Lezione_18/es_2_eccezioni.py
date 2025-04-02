def validate_password(password:str):
    upper:int = 0
    special:int = 0
    for i in password:
        if i.isupper():
            upper += 1
        elif i.isalnum():
            special += 1
    
    if len(password) >= 20 and upper >= 3 and special >= 4:
        return print(True)
    else:
        raise Exception("la password è sbagliata")
    
validate_password("d")
