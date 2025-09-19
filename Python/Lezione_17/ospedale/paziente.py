from Python.Lezione_17.ospedale.persona import Persona

class Paziente(Persona):

    def __init__(self, name, last_name, idCode:str):
        super().__init__(name, last_name)

        self.set_idCode(idCode)

    def set_idCode(self, idCode):
        self.__idCode = idCode

    def get_idCode(self):
        return self.__idCode
    
    def patientInfo(self):
        print(f"Paziente: {self.__name} {self.__last_name} \nID: {self.__idCode}")