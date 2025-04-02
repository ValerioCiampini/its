def make_car(produttore:str, modello:str, color:str = None, tow_package:bool = None):
    if color == None and tow_package == None:
        car:dict = {"produttore":produttore, "modello":modello}
    elif color == None and tow_package != None:
        car:dict = {"produttore":produttore, "modello":modello, "tow package":tow_package}
    elif color != None and tow_package == None:
        car:dict = {"produttore":produttore, "modello":modello, "colore":color}
    else:
        car:dict = {"produttore":produttore, "modello":modello, "colore":color, "tow package":tow_package}
    
    return car
    

print(make_car("a", "b", color = "c"))