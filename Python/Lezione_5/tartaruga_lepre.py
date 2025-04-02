import random

lepre:str = 1
tartaruga:str = 1

percorso:list = []

for i in range(70):
    percorso.append("_")

def show_percorso():
    print(percorso)

def tartaruga_move():
    mossa_t = random.randint(1, 10)

    if mossa_t >= 1 and mossa_t <= 5:
        percorso.pop(tartaruga - 1)
        tartaruga += 3
        percorso.insert(tartaruga - 1, "T")
    elif mossa_t >= 6 and mossa_t <= 7:
        percorso.pop(tartaruga - 1)
        if tartaruga >= 1 and tartaruga <= 6:
            tartaruga = 1
        else:
            tartaruga -= 6
        percorso.insert(tartaruga - 1, "T")
    else:
        percorso.pop(tartaruga - 1)
        tartaruga += 1
        percorso.insert(tartaruga - 1, "T")