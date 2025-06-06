def prodotti_(prodotti:dict):
    nuovi_prodotti:dict = {}

    for key, value in prodotti.items():
        if value < 50:
            nuovi_prodotti[key] = round(value + ((value / 100) * 10), 2)

    return nuovi_prodotti

print(prodotti_({"a":20, "b":55, "c":15}))