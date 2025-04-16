from persona import Persona

class Studente(Persona):
    
    def __init__(self, name:str, lastname:str, età:int, matricola:str):
        super().__init__(name, lastname, età)
        self.setMatricola(matricola)

    def __str__(self):
        return super().__str__() + f"\nmatricola: {self.matricola}"

    def setMatricola(self, matricola) -> None:
        if matricola:
            self.matricola = matricola
        else:
            print("la matricola non può essere vuota")

    def getMatricola(self) -> str:
        return self.matricola