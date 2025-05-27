from mytypes import Telefono

class Dipartimento:
    _nome:str
    _telefono:set[Telefono]
    _indirizzo:Indirizzo

    def nome(self):
        return self._nome
    
    def telefono(self):
        return self._telefono
    
    def indirizzo(self):
        return self._indirizzo
    
    def set_nome(self, _nome):
        self._nome = _nome

    def set_nome(self, _telefono):
        self._telefono = _telefono

    def set_nome(self, _indirizzo):
        self._indirizzo = _indirizzo