from __future__ import annotations
from mytypes import *
from datetime import datetime


class Persona:
    _nome: str
    _cognome: str
    _cf: list[Cf] # [1..*]
    _genere: Genere
    _maternita: IntGEZ|None # [0..1] - deve avere un valore se e solo se _genere = Genere.donna
    _posizione_mil: PosizioneMilitare | None # [0..1] da aggregazione, deve avere un valore se e solo se _genere = Genere.uomo
    _nascita: datetime
    def _init_(self, *, nome: str, cognome: str, cf: list[Cf], genere: Genere, maternita: IntGEZ|None=None, posizione_mil: PosizioneMilitare, nascita: datetime) -> None:
        self._nome = nome
        self._cognome = cognome
        self._nascita = nascita
        self._posizione_mil = posizione_mil
        if not cf:
            raise ValueError("La persona deve avere almeno un codice fiscale!")

        if genere == Genere.donna:
            if maternita is None:
                raise ValueError("È obbligatorio fornire il numero di maternità per le donne")
            self.diventa_donna(maternita)

        if genere == Genere.uomo:
            if posizione_mil is None:
                raise ValueError("E' obbligatorio fornire la posizione militare")
            self.set_posizione_mil(posizione_mil)

    def nome(self) -> str:
        return self._nome

    def cognome(self) -> str:
        return self._cognome

    def nascita(self) -> datetime:
        return self._nascita
    
    def set_nome(self, n: str) -> None:
        self._nome: str = n

    def set_cognome(self, c: str) -> None:
        self._cognome: str = c

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
        
    def posizione_mil(self) -> str:
        return self._posizione_mil
    
    def set_posizione_mil(self, posizione_mil: PosizioneMilitare) -> None:
        self._posizione_mil = posizione_mil


class Impiegato(Persona):
    _stipendio: RealGEZ
    _ruolo: Ruolo
    _is_responsabile: bool | None #[0..1]
    _progetto: set[tuple[Progetto, resp_prog._link]]

    def _init_(self, *, nome, cognome, cf, genere, maternita = None, nascita, stipendio: RealGEZ, ruolo: Ruolo, isresponsabile: bool | None=None) -> None:
        super()._init_(nome=nome, cognome=cognome, cf=cf, genere=genere, maternita=maternita, nascita=nascita)
        self.set_stipendio(stipendio)
        self._setruolo(ruolo)
        if isresponsabile is not None and ruolo != Ruolo.progettista:
            raise ValueError("Solamente i progettisti possono essere responsabili")
        elif ruolo == Ruolo.progettista and isresponsabile is None:
            raise ValueError("Bisogna indicare se il progettista è responsabile o no")
        self._isresponsabile(isresponsabile)
        self._progetto = set()

    def stipendio(self) -> RealGEZ:
        return self._stipendio
    
    def ruolo(self) -> Ruolo:
        return self._ruolo
    
    def isresponsabile(self) -> bool:
        return self._is_responsabile
    
    def set_isresponsabile(self, isresponsabile: bool):
        if self.ruolo() != Ruolo.progettista:
            raise ValueError("Solamente i progettisti possono essere responsabili")
        self._is_responsabile = isresponsabile
    
    def set_ruolo(self, ruolo: Ruolo, isresponsabile: bool|None  = None) -> None:
        self._ruolo = ruolo
        if ruolo != Ruolo.progettista:
            isresponsabile = None
        else:
            if isresponsabile is None:
                raise ValueError("Quando un impiegato diventa progettista bisogna indicare se è responsabile o meno")
            self.set_isresponsabile(isresponsabile)
    
    def set_stipendio(self, stipendio: RealGEZ) -> None:
        self._stipendio = stipendio

    def diventa_segretario(self) -> Ruolo:
        self.set_ruolo(Ruolo.segretario)

    def diventa_direttore(self) -> Ruolo:
        self.set_ruolo(Ruolo.direttore)

    def diventa_progettista(self) -> Ruolo:
        self.set_ruolo(Ruolo.progettista)
        self.set_is_responsabile() = True

    def add_progetto(self, progetto: Progetto)-> None:
        if self.is_responsabile():
            if progetto in self._progetto:
                raise ValueError
            r = resp_prog._link(progetto, self)
            t = tuple(progetto, r)
            self._progetto.add(t)
        
    def remove_progetto(self, progetto: 'Progetto', r: resp_prog._link) -> None:
        for t in self._progetto:
            x,y = t
            if x == progetto:
                self._progetto.remove(t)
                break



class Studente(Persona):
    def _init_(self, *, nome, cognome, cf, genere, maternita = None, nascita, matricola: IntGEZ) -> None:
        super()._init_(nome=nome, cognome=cognome, cf=cf, genere=genere, maternita=maternita, nascita=nascita)
        self._matricola = matricola

    def matricola(self):
        return self._matricola


class Progetto:
    _nome: str #noto alla nascita
    _impiegato: set[tuple[Impiegato, resp_prog._link]]


    def _init_(self, nome: str) -> None:
        self._nome = nome
        self._impiegato = set()

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, n: str) -> None:
        self._nome: str = n
    
    def add_impiegato(self, impiegato: Impiegato)-> None:
        if impiegato in self._impiegato:
            raise ValueError
        r = resp_prog._link(impiegato, self)
        t = tuple(impiegato, r)
        self._impiegato.add(t)
    
    def remove_impiegato(self, impiegato: 'Impiegato', r: resp_prog._link) -> None:
        for t in self._impiegato:
            x,y = t
            if x == impiegato:
                self._impiegato.remove(t)
                break

        

    
class PosizioneMilitare:
    _nome: str #<<immutable>>

    def _init_(self, nome: str) -> str:
        self._nome = nome

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, n: str) -> None:
        self._nome: str = n


class  resp_prog:
    class _link:
        _impiegato:Impiegato #non noto alla nascita
        _progetto:Progetto #non noto alla nascita

        def init(self, impiegato, progetto):
            self.set_impiegato(impiegato)
            self.set_progetto(progetto)

        def impiegato(self) -> Impiegato:
            return self._impiegato

        def progetto(self) ->Progetto:
            return self._progetto

        def set_impiegato(self, impiegato:Impiegato) -> None:
            self._impiegato = impiegato

        def set_progetto(self, progetto:Progetto) -> None:
            self._progetto = progetto