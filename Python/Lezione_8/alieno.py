class Alieno:

    def __init__(self, galaxy:str):
        self.set_galaxy(galaxy)

    def set_galaxy(self, galaxy:str) -> None:
        if galaxy != "":
            self.galaxy = galaxy
        else:
            print("Errore! La galassia di provenienza non può essere una stringa vuota")

    def get_galaxy(self) -> str:
        return self.galaxy
    
    def speak(self) -> None:
        print(f"\njnfjdnbui")

    def __str__(self) -> str:
        return f"\nAlieno proveniente dalla galassia {self.get_galaxy()}!\n"