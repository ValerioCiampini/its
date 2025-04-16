from persona import Persona
from studente import Studente

p:Persona = Persona("Valerio", "Ciampini", 20)

print(p)

studente1:Studente = Studente("Mario", "Rossi", 20, "0123456")

print(studente1)

if isinstance(studente1, Studente):
    print("studente 1 è una istanza della classe Studente")
else:
    print("studente 1 non è una istanza della classe Studente")

if isinstance(studente1, Persona):
    print("studente 1 è una istanza della classe Studente e Persona")
else:
    print("studente 1 non è una istanza della classe Studente e Persona")

if isinstance(p, Persona):
    print("p è un istanza di una classe Persona")
else:
    print("p non è un istanza di una classe Persona")

if isinstance(p, Studente):
    print("p è un istanza di una classe Persona e Studente")
else:
    print("p non è un istanza di una classe Studente")

if issubclass(Studente, Persona):
    print("Studente è una sottoclasse della classe Persona")
else:
    print("Studente non è una sottoclasse della classe Persona")