from types_ebuy import *
from datetime import *

class Bid:
    _istante:datetime

    def __init__(self, istante:datetime):
        self.set_istante(istante)

    def set_istante(self, istante):
        self._istante = istante

    def istante(self):
        return self._istante