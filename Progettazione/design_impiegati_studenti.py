from __future__ import annotations
from mytypes import *


class Persona:
    _nome: str
    _cognome: str
    _cf: list[Cf] # [1..*]
    _genere: Genere
    _maternita: IntGEZ # [0..1] - deve avere un valore se e solo se _genere = Genere.donna
    _posizione_mil: PosizioneMilitare | None # [0..1] da aggregazione, deve avere un valore se e solo se _genere = Genere.uomo

    def __init__(self, *, nome: str, cognome: str, cf: list[Cf], genere: Genere, maternita: IntGEZ|None=None) -> None:
        self._nome = nome
        self._cognome = cognome
        if not cf:
            raise ValueError("La persona deve avere almeno un codice fiscale!")

        if genere == Genere.donna:
            if maternita is None:
                raise ValueError("È obbligatorio fornire il numero di maternità per le donne")
            self.diventa_donna(maternita)

    def diventa_donna(self, maternita: IntGEZ) -> None:
        if self._genere == Genere.donna:
            raise RuntimeError("La persona era già una donna!")
        self._genere = Genere.donna
        self.set_maternita(maternita)
        self.__dimentica_uomo()

    def __dimentica_uomo(self) -> None:
        # Questo metodo è privato perché non deve essere mai invocato dall'esterno, ma solo all'interno di questa classe
        self._posizione_mil = None

    def set_maternita(self, maternita: IntGEZ) -> None:
        if not self._genere == Genere.donna:
            raise RuntimeError("Gli uomini non hanno il numero di maternità!")


class Impiegato(Persona):
    _stipendio:RealGEZ 
    _ruolo:Ruolo
    _is_responsabile:bool #[0..1]

    def __init__(self, *, nome, cognome, cf, genere, maternita = None, stipendio, ruolo:Ruolo):
        super().__init__(nome=nome, cognome=cognome, cf=cf, genere=genere, maternita=maternita)
        self.set_stipendio(stipendio)
        self.set_ruolo(ruolo)
        self.set_is_responsabile()

    def stipendio(self):
        return self._stipendio
    
    def ruolo(self):
        return self._ruolo
    
    def is_responsabile(self):
        return self._is_responsabile
    
    def set_stipendio(self, stipendio):
        self._stipendio = stipendio

    def set_ruolo(self, ruolo):
        self._ruolo = ruolo

    def set_is_responsabile(self):
        if self.ruolo == Ruolo.progettista:
            self._is_responsabile = True
        else:
            self._is_responsabile = False
    
    def diventa_segretario(self):
        if self._ruolo == Ruolo.segretario:
            raise RuntimeError("La persona era già un segretario!")
        self._ruolo = Ruolo.segretario

    def diventa_direttore(self):
        if self._ruolo == Ruolo.direttore:
            raise RuntimeError("La persona era già un direttore!")
        self._ruolo = Ruolo.direttore

    def diventa_progettista(self):
        if self._ruolo == Ruolo.progettista:
            raise RuntimeError("La persona era già un direttore!")
        self._ruolo = Ruolo.progettista
        self.set_is_responsabile()

class Studente(Persona):
    _matricola:IntGZ #{id} <<immutable>>

    def __init__(self, *, nome, cognome, cf, genere, maternita = None, matricola):
        super().__init__(nome=nome, cognome=cognome, cf=cf, genere=genere, maternita=maternita)
        self._matricola = matricola

    def matricola(self):
        return self._matricola
    
class Progetto:
    _nome:str

    def __init__(self, nome):
        self.set_nome(nome)

    def nome(self):
        return self._nome
    
    def set_nome(self, nome):
        self._nome = nome

class PosizioneMilitare:
    _nome:str #{id} <<immutable>>

    def __init__(self, nome):
        self._nome = nome

    def nome(self):
        return self._nome
    
class resp_prog:
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