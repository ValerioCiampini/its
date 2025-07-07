class Specie:

    def __init__(self, nome:str, popolazione:int, tasso_crescita:float):
        self.nome = nome
        self.popolazione = popolazione
        self.tasso_crescita = tasso_crescita

    def cresci(self):
        self.popolazione = self.popolazione * (1 + self.tasso_crescita/100)

    def anni_per_superare(self, altra_specie):
        count:int = 1
        while self.popolazione < altra_specie.popolazione:
            self.cresci()
            altra_specie.cresci()
            count += 1


        return count
    
    def getDensita(self, area_kmq: float):
        count:int = 0
        densità:float = self.popolazione / area_kmq
        while True:
            if densità == 1:
                break
            self.cresci()
            densità = self.popolazione / area_kmq
            count += 1

        return count

class BufaloKlingon(Specie):

    def __init__(self, popolazione, tasso_crescita, nome = "Bufalo Klingon"):
        super().__init__(nome, popolazione, tasso_crescita)

class Elefante(Specie):

    def __init__(self, popolazione, tasso_crescita, nome='Elefante'):
        super().__init__( nome, popolazione, tasso_crescita)
    


# Creazione delle istanze delle specie
bufalo_klingon = BufaloKlingon(100, 15)  # Crea un'istanza di BufaloKlingon con popolazione 100 e tasso di crescita 15%
elefante = Elefante(10, 35)  # Crea un'istanza di Elefante con popolazione 10 e tasso di crescita 35%

# Calcolo degli anni necessari per superare
anni_necessari = elefante.anni_per_superare(bufalo_klingon)  # Calcola gli anni necessari affinché gli elefanti superino i bufali Klingon
print(f"Anni necessari perché la popolazione di elefanti superi quella dei bufali Klingon: {anni_necessari}")

# Calcolo della densità di popolazione per i Bufali Klingon
anni_densita = bufalo_klingon.getDensita(1500)  # Calcola gli anni necessari per raggiungere una densità di 1 bufalo Klingon per km²
print(f"Anni necessari per raggiungere una densità di 1 Bufalo Klingon per km {anni_densita}")