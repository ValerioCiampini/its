class Persona:
        def __init__(self):
                self.name = ""
                self.lastname = ""
                self.età = 0

    
        def displayData(self) -> None:
                print(f"nome:{self.name}\ncognome:{self.lastname}\netà:{self.età}")

        def setName(self, name:str) -> None:
                self.name = name

        def setLastname(self, lastname:str) -> None:
                self.lastname = lastname

        def setEtà(self, età:int) -> None:
                if età < 0 or età > 130:
                        self.età = 0
                else:
                        self.età = età
        
        def getName(self) -> str:
                return self.name


     