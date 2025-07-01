class Media:

    def __init__(self, title:str, reviews:list[int]):
        self.set_title(title)
        self.reviews = reviews

    def get_title(self):
        return self.title
    
    def set_title(self, title):
        self.title = title

    def aggiungiValutazione(self, voto):
        if voto >= 1 or voto <= 5:
            self.reviews.append(voto)

    def get_media(self):
        somma = 0
        for i in self.reviews:
            somma += i

        media = somma / len(self.reviews)

        return media
    
    def getRate(self):
        if self.get_media() <= 1.4:
            return "Terribile"
        elif self.get_media() <= 2.4:
            return "Brutto"
        elif self.get_media() <= 3.4:
            return "Normale"
        elif self.get_media() <= 4.4:
            return "Bello"
        else:
            return "Grandioso"
        
    def ratePercentage(self, voto):
        counter = 0
        for i in self.reviews:
            if voto == i:
                counter += 1
        
        percentuale = (counter * 100) / len(self.reviews)

        return percentuale
    
    def recensione(self):
        return f"Titolo del Film: {self.get_title()}\nVoto Medio: {self.get_media()}\nGiudizio: {self.getRate()}\nTerribile: {self.ratePercentage(1)}%\nBrutto: {self.ratePercentage(2)}%\nNormale: {self.ratePercentage(3)}%\nBello: {self.ratePercentage(4)}%\nGrandioso: {self.ratePercentage(5)}%"
            
        
class File(Media):

    def __init__(self, title):
        super().__init__(title)