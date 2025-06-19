from mytypes import RealGEZ

class Progetto:
    _nome:str #noto alla nascita
    _budget:RealGEZ #noto alla nascita
    
    def __init__(self, nome:str, budget:RealGEZ):
        self.set_nome(nome)
        self.set_budget(budget)

    def nome(self):
        return self._nome
    
    def budget(self):
        return self._budget
    
    def set_nome(self, nome):
        self._nome = nome

    def set_budget(self, budget):
        self._budget = budget

   