from Python.Lezione_17.ospedale.persona import Persona

class Dottore(Persona):

    def __init__(self, name, last_name, specialization, parcel):
        super().__init__(name, last_name)

        if isinstance(specialization, str) == False:
            self.__specialization = None
            raise ValueError("La specializzazione inserita non è una stringa!")
        else:
            self.set_specialization(specialization)

        if isinstance(parcel, float) == False:
            self.__parcel = None
            raise ValueError("La parcella inserita non è un float!")
        else:
            self.set_parcel(parcel)

    def set_specialization(self, specialization):
        if isinstance(specialization, str):
            self.__specialization = specialization
        else:
            raise ValueError("La specializzazione inserita non è una stringa!")
        
    def set_parcel(self, parcel):
        if isinstance(parcel, float):
            self.__parcel = parcel
        else:
            raise ValueError("La parcella non è un float!")
        
    def get_specialization(self):
        return self.__specialization
    
    def get_parcel(self):
        return self.__parcel
    
    def isAValidDoctor(self):
        if self.__age > 30:
            print(f"Doctor {self.__name} {self.__last_name} is valid")
            return True
        else:
            print(f"Doctor {self.__name} {self.__last_name} is not valid")
            return False

    def doctorGreet(self):
        super().greet()
        print(f"Sono un medico {self.__specialization}")

