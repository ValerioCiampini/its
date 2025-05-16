from enum import *

class Genere(StrEnum):
    uomo = auto()
    donna = auto()

class Voto:
    v:int

    def __init__(self, v:int):
        if v < 18 or v > 31:
            raise ValueError(f"il voto = {v} deve essere tra 18 e 31")
        
        self.v = v

    def __eq__(self, other):
        return self.v == other.v
        

print("__name__ all'interno di mytypes.py: " + __name__)

if __name__ == "__main__":

    print("Test di python.py\n==============\n")
    print(Genere.uomo)
    print(Genere.donna.upper())
    print(Genere.donna[:2])

l = [Voto(18), Voto(21)]
x = Voto(18)

print(x in l)