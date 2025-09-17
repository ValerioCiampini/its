from dottore import Dottore
from paziente import Paziente


class Fattura:

    def __init__(self, patient:list[Paziente], doctor:Dottore):
        if doctor.isAValidDoctor():
            self.fatture = len(patient)
            self.salary = 0
        else:
            self.patient = None
            self.fatture = None
            self.salary = None
            self.doctor = None
            raise ValueError("Non è possibile creare la classe fattura poichè il dottore non è valido!")
        
    def get_salary(self):
        self.salary = self.doctor.get_parcel() * len(self.patient)
        return self.salary
    
    def get_fatture(self):
        self.get_fatture = len(self.patient)
        return self.fatture
    
    def addPatient(self, newPatient:Paziente):
        self.patient.append(newPatient)
        self.get_fatture() 
        self.get_salary()
        print(f"Alla lista del Dottor {self.doctor.get_last_name()} è stato aggiunto il paziente {self.newPatient.get_idCode()}")
    
    def removePatient(self, idCode:str):
        self.patient.remove(idCode)
        self.get_fatture()
        self.get_salary()
        print(f"Alla lista del Dottor {self.doctor.get_last_name()} è stato rimosso il paziente {idCode}")
        