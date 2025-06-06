def classificazioni(lista:list[int]):
    
    dict1:dict = {}
    positivi:list = []
    negativi:list = []
    
    for i in lista:
        if i < 0:
            negativi.append(i)
        else:
            positivi.append(i)

    dict1["positivi"] = positivi
    dict1["negativi"] = negativi

    return dict1

print(classificazioni([1, 2, -3, 4, -5, -6]))