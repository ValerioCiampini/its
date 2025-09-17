from persona import Persona
from dottore import Dottore
from paziente import Paziente
from fattura import Fattura

doc1:Dottore = Dottore("Totti", "Gol", "Calciatore", 3.6)
doc2:Dottore = Dottore("Mario", "Rossi", "Fisioterapista", 90)

paz1:Paziente = Paziente("Paolo","Pimenta", "123")
paz2:Paziente = Paziente("Moise", "Kean", "456")
paz3:Paziente = Paziente("Primo", "Secondo", "789")
paz4:Paziente = Paziente("Marco", "Polo", "159")

pazienti1:list[Paziente] = [paz1, paz3, paz4]
pazienti2:list[Paziente] = [paz2]

doc1.set_age(48)
doc2.set_age(65)

doc1.greet()
doc2.greet()

fat1:Fattura = Fattura(pazienti1, doc2)
fat2:Fattura = Fattura(pazienti2, doc1)

print(f"Salario {doc2.get_last_name()}: {fat1.get_salary()} euro")
print(f"Salario {doc1.get_last_name()}: {fat2.get_salary()} euro")