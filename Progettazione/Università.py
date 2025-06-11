from mytypes import *
from datetime import *

class Facoltà:
    _nome:str #noto alla nascita
    _tipo_facoltà:str #noto alla nascita

    def __init__(self, nome:str, tipo_facolta:str) -> None:
        self.set_nome(nome)
        self.set_tipo_facoltà(tipo_facolta)

    def nome(self) -> str:
        return self._nome
    
    def tipo_facoltà(self) -> str:
        return self._tipo_facoltà
    
    def set_nome(self, nome:str) -> None:
        self._nome = nome

    def set_tipo_facoltà(self, tipo_facoltà:str) -> None:
        self._tipo_facoltà = tipo_facoltà   

class Corso:
    _nome:str #noto alla nascita
    _codice:str #noto alla nascita
    _durata_ore:RealGEZ #noto alla nascita

    def __init__(self, nome:str, codice:str, durata_ore:RealGEZ) -> None:
        self.set_nome(nome)
        self.set_codice(codice)
        self.set_durata_in_ore(durata_ore)

    def nome(self) -> str:
        return self._nome

    def codice(self) -> str:
        return self._codice
    
    def durata_in_ore(self) -> RealGEZ:
        return self._durata_ore
    
    def set_nome(self, nome) -> None:
        self._nome = nome

    def set_codice(self, codice) -> None:
        self._codice = codice

    def set_durata_in_ore(self, durata_ore) -> None:
        self._durata_in_ore = durata_ore

class Studente:
    _nome:str #noto alla nascita
    _codice_fiscale:Cf #noto alla nascita
    _data_nascita:date #noto alla nascita <<immutable>>
    _anno_iscrizione:IntG1088 #noto alla nascita <<immutabile>>
    _matricola:str #noto alla nascita <<immutabile>>
    _corso_superato:Corso 

    def __init__(self, nome:str, codice_fiscale:Cf, data_nascita:date, anno_iscrizione:IntG1088, matricola:str, corso_superato:Corso) -> None:
        self.set_nome(nome)
        self.set_codice_fiscale(codice_fiscale)
        self._data_nascita = data_nascita
        self._anno_iscrizione = anno_iscrizione
        self._matricola = matricola
        self.set_corso_superato(corso_superato)

    def nome(self) -> str:
        return self._nome
    
    def codice_fiscale(self) -> Cf:
        return self._codice_fiscale
    
    def data_nascita(self) -> date:
        return self._data_nascita
    
    def anno_iscrizione(self) -> IntG1088:
        return self._anno_iscrizione
    
    def matricola(self) -> str:
        return self._matricola
    
    def corso_superato(self) -> Corso:
        return self._corso_superato
    
    def set_nome(self, nome:str) -> None:
        self._nome = nome

    def set_codice_fiscale(self, codice_fiscale:Cf) -> None:
        self._codice_fiscale = codice_fiscale

    def set_corso_superato(self, corso_superato:Corso) -> None:
        self._corso_superato = corso_superato

class Professore:
    _nome:str #noto alla nascita
    _data_nascita:date #noto alla nascita <<immutable>>
    _codice_fiscale:Cf #noto alla nascita
    _corso_superato:Corso

    def __init__(self, nome:str, codice_fiscale:Cf, data_nascita:date, corso_superato:Corso) -> None:
        self.set_nome(nome)
        self.set_codice_fiscale(codice_fiscale)
        self._data_nascita = data_nascita
        self.set_corso_superato(corso_superato)

    def nome(self) -> str:
        return self._nome
    
    def codice_fiscale(self) -> Cf:
        return self._codice_fiscale

    def data_nascita(self) -> date:
        return self._data_nascita
        
    def corso_superato(self) -> Corso:
        return self._corso_superato
    
    def set_nome(self, nome:str) -> None:
        self._nome = nome

    def set_codice_fiscale(self, codice_fiscale:Cf) -> None:
        self._codice_fiscale = codice_fiscale

    def set_corso_superato(self, corso_superato:Corso) -> None:
        self._corso_superato = corso_superato

class Città:
    _nome:str #noto alla nascità

    def __init__(self, nome:str) -> None:
        self.set_nome(nome)

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome:str) -> None:
        self._nome:str = nome

class Regione:
    _nome:str #noto alla nascità

    def __init__(self, nome:str) -> None:
        self.set_nome(nome)

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome:str) -> None:
        self._nome = nome


