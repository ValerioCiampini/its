n:int = int(input("inserisci un numero n: "))
result:int = 0

for i in range(n):
    x:int = int(input("inserisci un numero x: "))
    y:int = int(input("inserisci un numero y: "))

    if x > 0 and y > 0:
        result = x * y
        print(result)
    elif x < 0 and y < 0:
        print("errore")
    else:
        result =  x - y
        print(result)