from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def __init__(self):
        pass 

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimetro(self) -> float:
        pass