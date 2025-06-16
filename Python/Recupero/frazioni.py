class Frazione:
    __denominatore:int
    __numeratore:int

    def __init__(self, denominatore:int, numeratore:int):
        self.set_denominatore(denominatore)
        self.set_numeratore(numeratore)

    def denominatore(self):
        return self.__denominatore
    
    def numeratore(self):
        return self.__numeratore
    
    def set_denominatore(self, denominatore:int):
        self.__denominatore = denominatore

    def set_numeratore(self, numeratore:int):
        self.__numeratore = numeratore

    def value()