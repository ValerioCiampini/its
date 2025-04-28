from persona import Persona
from alieno import Alieno

p:Persona = Persona("Valerio", "Ciampini", 20)
print(p)

et:Alieno = Alieno("Andromeda")
print(et)

p.speak()

et.speak()