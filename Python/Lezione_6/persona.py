class Persona:
    def __init__(self, name:str, lastname:str, età:int):
        self.name = name
        self.lastname = lastname
        self.età = età

    def displayData(self) -> None:
        print(f"nome:{self.name}\ncognome:{self.lastname}\netà:{self.età}")