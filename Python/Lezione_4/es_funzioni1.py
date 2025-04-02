def calcolo(x, y):
    somma:int = 0
    for i in range(x, y+1):
        somma += i
    return somma

print("la somma dei numeri tra 1 e 10 è", calcolo(1, 10))
print("la somma dei numeri tra 20 e 37 è", calcolo(20, 37))
print("la somma dei numeri tra 35 e 49 è", calcolo(35, 49))