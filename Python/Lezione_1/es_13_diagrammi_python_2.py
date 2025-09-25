x:int = int(input("inserisci un numero x: "))
y:int = int(input("inserisci un numero y: "))
z:int = int(input("inserisci un numero z: "))

while True:
    if x % 1 == 0 and x > 0:
        if y % 1 == 0 and y > 0:
            if z % 1 == 0 and z > 0:
                break
            else:
                print("z deve essere positivo e positivo")
                x:int = int(input("inserisci un numero x: "))
                y:int = int(input("inserisci un numero y: "))
                z:int = int(input("inserisci un numero z: "))
        else:
            print("y deve essere positivo e positivo")
            x:int = int(input("inserisci un numero x: "))
            y:int = int(input("inserisci un numero y: "))
            z:int = int(input("inserisci un numero z: "))
    else:
        print("x deve essere positivo e positivo")
        x:int = int(input("inserisci un numero x: "))
        y:int = int(input("inserisci un numero y: "))
        z:int = int(input("inserisci un numero z: "))

if (x + y + z) % 2 == 0 and x % 3 == 0 and y % 5 == 0 and z % 7 == 0:
    print("regole rispettate")
else:
    print("regole non rispettate")