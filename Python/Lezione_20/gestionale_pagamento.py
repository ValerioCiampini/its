class Pagamento:

    def __init__(self):
        
        self.__importo = 0

    def set_importo(self, importo:float):
        self.__importo = importo

    def get_importo(self):
        return self.__importo
    
    def dettagliPagamento(self):
        print(f"Importo del pagamento: {round(self.get_importo(), 2)} euro")

class PagamentoContanti(Pagamento):
    
    def __init__(self, importo:float):
        super().__init__()

        self.__importo = importo

    def dettagliPagamento(self):
        print(f"Importo del pagamento: {round(self.__importo, 2)} euro in contanti")

    def inPezziDa(self):

        banconote = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]

        soldi_usati:dict = {}

        for i in banconote:
            if self.__importo < i:
                continue
            else:
                while (self.__importo - i) >= 0:
                    self.__importo -= i
                    if i in soldi_usati:
                        soldi_usati[i] += 1
                    else:
                        soldi_usati[i] = 1
                if i in soldi_usati:
                    soldi_usati[i] += 1
                else:
                    soldi_usati[i] = 1

        print(f"{self.__importo} euro da pagare in contanti con:")
            
        for key, value in soldi_usati.items():
            if key < 5:
                print(f"{value} moneta da {key} euro")
            else:
                print(f"{value} banconote da {key} euro")

class PagamentoCartaDiCredito(Pagamento):

    def __init__(self, importo:float, nome:str, data:str, numero:int):
        super().__init__()

        self.__importo = importo
        self.__nome = nome
        self.__data = data
        self.__numero = numero

    def dettagliPagamento(self):
        print(f"Pagamento di: {self.__importo} effetuato con la carta di credito\nNome sulla carta: {self.__nome}\nData di scadenza: {self.__data}\nNumero della carta: {self.__numero}")


if __name__ == "__main__":
    p1 = PagamentoContanti(150.00)
    p2 = PagamentoContanti(95.25)

    p1.inPezziDa()
    p2.inPezziDa()

    p3 = PagamentoCartaDiCredito(200, "d", "y", 3)
    p4 = PagamentoCartaDiCredito(365, "e", "6", 76)

    for i in [p1, p2, p3, p4]:
        i.dettagliPagamento()
    