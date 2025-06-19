from dipartimento import Dipartimento
from impiegato import Impiegato

class Direzione:
    
    class _link:

        _dipartimento: Dipartimento #noto alla nascita
        _impiegati: set[Impiegato] #non noto alla nascita

        def __init__(self, dipartimento, impiegato):
            self.set_dipartimento(dipartimento)
            self.set_impiegato(impiegato)

        def dipartimento(self):
            return self._dipartimento
        
        def impiegato(self):
            return frozenset[self._impiegati]
        
        def set_dipartimento(self, dipartimento:Dipartimento):
            self._dipartimento = dipartimento

        def set_impiegato(self, impiegati:set[Impiegato]):
            self._impiegati = impiegati