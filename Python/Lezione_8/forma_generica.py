from abc import ABC, abstractmethod

class Forma_generica(ABC):

    @abstractmethod
    def draw(self) -> None:
        pass

    def set_shape(self, shape) -> None:
        if shape != "":
            self.shape = shape
        else:
            print("Errore! shape non può essere una lista vuota")

    def get_shape(self) -> str:
        return self.shape