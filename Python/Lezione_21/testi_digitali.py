class Documento:

    def __init__(self, testo:str):
        self.set_testo(testo)

    def get_testo(self):
        return self.testo
    
    def set_testo(self, testo):
        self.testo = testo

    def isintesto(self, parola):
        testo = self.get_testo().split(" ")
        for i in testo:
            if parola.lower() == i.lower():
                return True 
        
        return False
            
class Email(Documento):

    def __init__(self, testo, mittente:str, destinatario:str, titolo:str):
        super().__init__(testo)
        self.set_mittente(mittente)
        self.set_destinatario(destinatario)
        self.set_titolo(titolo)

    def get_destinatario(self):
        return self.destinatario
    
    def get_mittente(self):
        return self.mittente
    
    def get_titolo(self):
        return self.titolo
    
    def set_destinatario(self, destinatario):
        self.destinatario = destinatario

    def set_mittente(self, mittente):
        self.mittente = mittente

    def set_titolo(self, titolo):
        self.titolo = titolo

    def get_testo(self):
        return f"Da: {self.get_mittente()}, A: {self.get_destinatario()}\nTitolo: {self.get_titolo()}\nMessaggio: {super().get_testo()}"
    
    def writetoFile(self, file):
        with open(file, "w") as f:
            f.write(self.get_testo())

class File(Documento):

    def __init__(self, nomepercorso):
        self.nomepercorso = nomepercorso
        super().__init__(self.leggiTestoDaFile())
        
    def leggiTestoDaFile(self):
        with open(self.nomepercorso, "r") as file:
            f = file.read()

        return f

    def get_testo(self):
        return f"Percorso: {self.nomepercorso}\nContenuto: {super().get_testo()}"
    

if __name__ == "__main__":
    e:Email = Email("Ciao", "Valerio", "Mattia", "Saluti")
    f:File = File("Python/Lezione 21/document.txt")

    print(e.get_testo())
    print(f.get_testo())

    e.writetoFile("Python/Lezione 21/email1.txt")

    print(e.isintesto("incontrarci"))
    print(f.isintesto("percorso"))




    

    

    
