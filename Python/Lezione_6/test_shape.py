from cerchio import Circle
from rettangolo import Rettangle

if __name__ == '__main__':
    c = Circle(20)
    print(round(c.area(), 2), c.perimetro())

    r = Rettangle(10, 30)
    print(round(r.area(), 2), r.perimetro())

