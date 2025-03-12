import math
temperature:dict = {"1":float(input("inserisci la temperatura di lunedì: ")), "2":float(input("inserisci la temperatura di martedì: ")), "3":float(input("inserisci la temperatura di mercoledì: ")), "4":float(input("inserisci la temperatura di giovedì: ")), "5":float(input("inserisci la temperatura di venerdì: ")), "6":float(input("inserisci la temperatura di sabato: ")), "7":float(input("inserisci la temperatura di domenica: "))}
min:float = math.inf
max:float = -math.inf
somma:float = 0
media:float = 0
norma:int = 0
nome_max:str = ""
nome_min:str = ""

for i, j in temperature.items():
    somma += j
    if j >= 10 and j <= 30:
        norma += 1
    elif j > 35 or j < 5:
        print("allerta temperatura")

    if j < min:
        min = j
        nome_min = i
    elif j > max:
        max = j
        nome_max = i

media = somma / 7
print(media)
print(f"il giorno comn la temperatura max è : {nome_max} con {max} gradi\n il giorno con la temperatura minima è {nome_min} con {min} gradi")


