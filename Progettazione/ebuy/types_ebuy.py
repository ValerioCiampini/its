from enum import *

class IntGZ(int):
    def __new__(cls, x:int|float|bool|str):
        n:int =  super().__new__(x)

        if n > 0:
            return n
        
        raise ValueError("Il valore non può essere minore o uguale a 0")
    
class RealGEZ(float):

    def __new__(cls, x:int|float|bool|str):
        n:float =  super().__new__(x)

        if n >= 0:
            return n
        
        raise ValueError("Il valore non può essere minore di 0")
    
class RealGEZ(float):

    def __new__(cls, x:int|float|bool|str):
        n:float =  super().__new__(x)

        if n > 0:
            return n
        
        raise ValueError("Il valore non può essere minore o uguale a 0")
    
class Condizione(StrEnum):
    ottimo = auto()
    buono = auto()
    discreto = auto()
    da_sistemare = auto()

class IntGEZ(int):
    def __new__(cls, x:int|float|bool|str):
        n:int =  super().__new__(x)

        if n >= 0:
            return n
        
        raise ValueError("Il valore non può essere minore di 0")
    
class RealGZ(float):

    def __new__(cls, x:int|float|bool|str):
        n:float =  super().__new__(x)

        if n > 0:
            return n
        
        raise ValueError("Il valore non può essere minore di 0")
    