class Contatore:
    
    def __init__(self):
        self.contatore = 0

    def setZero(self):
        self.contatore = 0

    def add1(self):
        self.contatore += 1

    def sub1(self):
        if self.contatore > 0:
            self.contatore -= 1
        else: 
            print("Non è possibile eseguire la sottrazione")
        
    def get(self):
        return self.contatore
    
    def mostra(self):
        print(self.contatore)
    