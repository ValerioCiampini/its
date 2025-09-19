from film import Film

class Azione(Film):

    def __init__(self, id, title):
        super().__init__(id, title)
        self.__genere = "Azione"
        self.__penale = 3

    def get_genere(self):
        return self.__genere
    
    def get_penale(self):
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorni):
        return giorni * self.__penale
    
class Commedia(Film):

    def __init__(self, id, title):
        super().__init__(id, title)
        self.__genere = "Commedia"
        self.__penale = 2.5

    def get_genere(self):
        return self.__genere
    
    def get_penale(self):
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorni):
        return giorni * self.__penale
    
class Dramma(Film):

    def __init__(self, id, title):
        super().__init__(id, title)
        self.__genere = "Dramma"
        self.__penale = 2

    def get_genere(self):
        return self.__genere
    
    def get_penale(self):
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorni):
        return giorni * self.__penale