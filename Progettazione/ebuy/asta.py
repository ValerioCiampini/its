from types_ebuy import *
from post_oggetto import PostOggetto
from datetime import *

class Asta(PostOggetto):
    _prezzo_bid:RealGZ
    _scadenza:datetime

    def __init__(self, prezzo, anni_garanzia, descrizione, is_nuovo, condizione, prezzo_bid:RealGZ, scadenza:datetime):
        super().__init__(PostOggetto, prezzo, anni_garanzia, descrizione, is_nuovo, condizione)
        self.set_prezzo_bid(prezzo_bid)
        self.set_scadenza(scadenza)
    
    def set_prezzo_bid(self, prezzo_bid):
        self._prezzo_bid = prezzo_bid

    def set_scadenza(self, scadenza):
        self._scadenza = scadenza

    def prezzo_bid(self):
        return self._prezzo_bid
    
    def scadenza(self):
        return self._scadenza