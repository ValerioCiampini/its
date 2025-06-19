from impiegato import Impiegato
from progetto import Progetto

class Coinvolto:

    @classmethod
    def add(cls, impiegato:Impiegato, progetto:Progetto):
        l = cls._link(impiegato, progetto)
        impiegato.add_link_coinvolto(l)
        progetto.add_link_coinvolto(l)
    
    class _link:
        _impiegato:set[Impiegato] #non noto alla nascita
        _progetto:set[Progetto] #non noto alla nascita

        def __init__(self, impiegato, progetto):
            self.set_impiegato(impiegato)
            self.set_progetto(progetto)

        def impiegato(self):
            return frozenset[self._impiegato]
    
        def progetto(self):
            return frozenset[self._progetto]
    
        def set_impiegato(self, impiegato:set[Impiegato]):
            self._impiegato = impiegato

        def set_progetto(self, progetto:set[Progetto]):
            self._progetto = progetto