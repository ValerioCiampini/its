class Specie:

    def __init__(self, nome:str, popolazione:int, tasso_crescita:float):
        self.nome = nome
        self.popolazione = popolazione
        self.tasso_crescita = tasso_crescita

    def cresci(self):
        self.popolazione = self.popolazione * (1 + self.tasso_crescita/100)

    def anni_per_superare(self, altra_specie):
        count:int = 0
        while self.popolazione < altra_specie.popolazione:
            self.cresci()
            altra_specie.cresci()
            count += 1


        return count
    
    def getDensita(self, area_kmq: float):
        count:int = 0
        densità:float = self.popolazione / area_kmq
        while densità != 1:
            self.cresci()
            count += 1

        return count


    

        