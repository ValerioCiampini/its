def is_valid_ipv4(address: str) -> bool:
    
    lista = address.split(".")
    
    if len(lista) != 4:
            return False
    
    for i in lista:

        if int(i) <= 0 or int(i) >= 255:
            return False
        elif i.isdigit() == False:
            return False

    return True
