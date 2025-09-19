from genere import *
from noleggio import *

f1:Azione = Azione(1, "a")
f2:Azione = Azione(2, "b")
f3:Azione = Azione(3, "c")
f4:Azione = Azione(4, "d")
f5:Azione = Azione(5, "e")
f6:Commedia = Commedia(6, "f")
f7:Commedia = Commedia(7, "g")
f8:Commedia = Commedia(8, "h")
f9:Commedia = Commedia(9, "i")
f10:Dramma = Dramma(10, "j")

n1:Noleggio = Noleggio([f1, f2, f3, f4, f5, f6, f7, f8, f9, f10])

print("Quale film vuoi nollegiare? ")

n1.rentAMovie(f2, 1)
n1.rentAMovie(f1, 1)

n1.rentAMovie(f1, 2)
n1.rentAMovie(f8, 2)

n1.giveBack(f1, 1, 50)

n1.printMovies()