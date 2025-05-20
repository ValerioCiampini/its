from shape import Shape
import math

class Rettangle(Shape):

    def __init__(self, base:float, altezza:float):
        super().__init__()
        self.base = base
        self.altezza = altezza

    def area(self):
        return (self.base * self.altezza) / 2
    
    def perimetro(self):
        return (self.base * 2) + (self.altezza * 2)