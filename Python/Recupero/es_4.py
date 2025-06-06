def condizioni(x:bool, y:bool, z:bool):
    if x == True and (y == True or z == True):
        print("Azione permessa")
    else:
        print("Azione negata")


condizioni(True, False, False)