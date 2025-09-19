from film import Film
from genere import *

class Noleggio:

    def __init__(self, film_list:list[Azione|Commedia|Dramma]):
        self.__film_list = film_list
        self.__rented_film:dict = {}

    def isAvaiable(self, film:Azione|Commedia|Dramma):
        if film in self.__film_list:
            print(f"Il film scelto è disponibile: {film.get_title()}")
            return True
        else:
            print(f"Il film scelto non è disponibile: {film.get_title()}")
            return False
    def rentAMovie(self, film:Azione|Commedia|Dramma, idCliente):
        if self.isAvaiable(film):
            self.__film_list.remove(film)

            if not idCliente in self.__rented_film:
                self.__rented_film[idCliente] = [film]
            else:
                self.__rented_film[idCliente].append(film)

            print(f"Il cliente {idCliente} ha noleggiato {film.get_title()}!")
        else:
            print(f"Non è possibile nolegiare il film {film.get_title()}!")

    def giveBack(self, film:Azione|Commedia|Dramma, idCliente, days):
        self.__rented_film[idCliente].remove(film)

        self.__film_list.append(film)

        tot = film.calcolaPenaleRitardo(days)

        print(f"Cliente: {idCliente}! La penale da pagare per il film {film.get_title()} e' di {tot} euro!")

    def printMovies(self):
        for i in self.__film_list:
            print(f"{i.get_title()} - {i.get_genere()}")
    
    def printRentMovies(self, idCliente):
        print(self.__rented_film[idCliente])
            
