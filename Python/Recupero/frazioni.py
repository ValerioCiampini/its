class Frazione:
    __denominatore:float
    __numeratore:float

    def __init__(self, denominatore:float, numeratore:float):
        self.set_denominatore(denominatore)
        self.set_numeratore(numeratore)

    def denominatore(self):
        return self.__denominatore
    
    def numeratore(self):
        return self.__numeratore
    
    def set_denominatore(self, denominatore:float):
        if not denominatore.is_integer() or denominatore == 0:
            self.__denominatore = 5
        else:
            self.__denominatore = denominatore

    def set_numeratore(self, numeratore:float):
        if not numeratore.is_integer():
            self.__denominatore == 13
        else:
            self.__numeratore = numeratore

    def value(self):
        return round(self.__numeratore / self.__denominatore, 3)

    def __str__(self):
        return f"{self.__numeratore} /  {self.__denominatore}"

def mcd(x:int, y:int):
    divisori_x:list[int] = []
    divisori_y:list[int] = []
    divisori_comuni:list[int] = []

    for i in range(1, x):
        if x % i == 0:
            divisori_x.append(i)

    for i in range(1, y):
        if y % i == 0:
            divisori_y.append(i)

    for i in x:
        if i in divisori_y:
            divisori_comuni.append(i)

    return max(divisori_comuni)

def semplifica(lista:list[Frazione]):
    lista_semplificata:list[Frazione] = []
    d:int = 2
    d1:int = 2

    for i in lista:
        numeratore:int = i.numeratore()
        denominatore:int = i.denominatore()
        
        while numeratore > 1:
            if numeratore % d == 0:
                numeratore //= d
            else:
                d += 1

        while denominatore > 1:
            if denominatore % d1 == 0:
                denominatore //= d1
            else:
                d1 += 1

        lista_semplificata.append(Frazione(denominatore, numeratore))

    return lista_semplificata

def fractionCompare(lista:list[Frazione], lista_semplificata:list[Frazione]):
    for i in lista:
        for j in lista_semplificata:
            if i.value() == j.value():
                print(f"Valore frazione originale: {i.value} --- Valore frazione ridotta: {j.value}")


