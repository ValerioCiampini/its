from enum import *
from typing import Any
from typing import Self

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
        
class Indirizzo:
    
    def __init__(self, via:str, civico:str, cap:str):
        if not isinstance(via, str) or not isinstance(civico, str) or not isinstance(cap, str):
            raise TypeError("Non hai inserito dati validi per un indirizzo")
        
        self.via = via
        self.civico = civico
        self.cap = cap

    def get_via(self):
        return self.via
    
    def get_civico(self):
        return self.civico
    
    def get_cap(self):
        return self.cap
    
    def __hash__(self):
        return hash((self.get_via(), self.get_civico(), self.get_cap()))
    
    def __eq__(self, other)->bool:
        if other is None or not isinstance(other, type(self)) or hash(self) != hash(other):
            return False
        return (self.get_via(), self.get_civico(), self.get_cap()) == (other.get_via(), other.get_civico(), other.get_cap())
    
class Email:
    domini:list = [".it", ".com"]
    def __init__(self, chiocciola, prima_parte, seconda_parte, dominio, domini):
        if not isinstance(prima_parte, str) or not chiocciola == "@" or isinstance(seconda_parte, str) or dominio not in domini:
            raise TypeError("Dati inseriti nell'email non validi")
        
        self.prima_parte = prima_parte
        self.seconda_parte = seconda_parte
        self.chiocciola = chiocciola
        self.dominio = dominio

    def get_prima_parte(self):
        return self.prima_parte
    
    def get_chiocciola(self):
        return self.chiocciola
    
    def get_seconda_parte(self):
        return self.seconda_parte
    
    def get_dominio(self):
        return self.dominio
    
    def __hash__(self):
        return hash((self.get_prima_parte(), self.get_chiocciola(), self.get_seconda_parte(), self.get_dominio()))
    
    def __eq__(self, other):
        if other is None or not isinstance(other, type(self)) or hash(self) != hash(other):
            return False
        return (self.get_prima_parte(), self.get_chiocciola(), self.get_seconda_parte(), self.get_dominio()) == (other.get_prima_parte(), other.get_chiocciola(), other.get_seconda_parte(), other.get_dominio())
    
class Telefono:

    def __init__(self, numero):
        if len(numero) != 10 and numero.isdigit():
            raise TypeError("Numero telefono non valido")
        
        self.numero = numero
    
    def get_numero(self):
        return self.numero
    
    def __hash__(self):
        return hash(self.get_numero())
    
    def __eq__(self, other):
        if other is None or not isinstance(other, type(self)) or hash(self) != hash(other):
            return False
        return (self.get_numero()) == (other.get_numero())
    
class Cf(str):
    def __new__(cls, value) -> Self:
        if not value.isalnum() or len(value) != 16:
            raise ValueError("Codice fiscale non valido")
        return str.__new__(cls, value)
    
class RealGEZ(float):

    def __new__(cls, x:int|float|bool|str):
        n:float =  super().__new__(x)

        if n >= 0:
            return n
        
        raise ValueError("Il valore non può essere minore di 0")
    
class IntGZ(int):
    def __new__(cls, x:int|float|bool|str):
        n:int =  super().__new__(x)

        if n > 0:
            return n
        
        raise ValueError("Il valore non può essere minore o uguale a 0")
    
class IntGEZ(int):
    def __new__(cls, x:int|float|bool|str):
        n:int =  super().__new__(x)

        if n >= 0:
            return n
        
        raise ValueError("Il valore non può essere minore di 0")
    
class IntGC(int):
    def __new__(cls, x:int|float|bool|str):
        n:int =  super().__new__(x)

        if n >= 1900:
            return n
        
        raise ValueError("Il valore non può essere minore di 1900")