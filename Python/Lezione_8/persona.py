class Persona:
    def __init__(self, name:str, lastname:str, età:int):
        self.setName(name)
        self.setLastname(lastname)
        self.setEtà(età)

    def __str__(self):
        return f"Name: {self.name}\nLastname: {self.lastname}\nAge: {self.età}"

    def setName(self, name:str) -> None:
        if name:
            self.name = name
        else:
            print("il nome non può essere una stringa vuota")

    def setLastname(self, lastname:str) -> None:
        if lastname:
            self.lastname = lastname
        else:
            print("il cognome non può essere una stringa vuota")

    def setEtà(self, età:int) -> None:
        if età < 0 or età > 130:
            self.età = 0
        else:
            self.età = età
        
    def getName(self) -> str:
        return self.name
    
    def getLastname(self) -> str:
        return self.lastname
    
    def getEtà(self) -> str:
        return self.età
    
    def speak(self) -> None:
        print(f"\nmy name is {self.name}!")