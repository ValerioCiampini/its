from datetime import date
from impiegato import Impiegato
from dipartimento import Dipartimento

class Afferenza:

    class _link:
        _impiegato:set[Impiegato] #non noto alla nascita
        _dipartimento:Dipartimento #non noto alla nascita
        _data_afferenza:date #noto alla nascita <<immutable>>

        def __init__(self, impiegato, dipartimento, data_afferenza):
            self.set_impiegato(impiegato)
            self.set_dipartimento(dipartimento)
            self._data_afferenza = data_afferenza

        def impiegato(self):
            return self._impiegato
        
        def dipartimento(self):
            return self._dipartimento
        
        def data_afferenza(self):
            return self._data_afferenza
        
        def set_impiegato(self, impiegato):
            self._impiegato = impiegato

        def set_dipartimento(self, dipartimento):
            self._dipartimento = dipartimento
