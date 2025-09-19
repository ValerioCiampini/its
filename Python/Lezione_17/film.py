class Film:

    def __init__(self, id:int, title:str):
        self.__id = self.set_id(id)
        self.__title = self.set_title(title)

    def set_id(self, id):
        self.__id = id

    def set_title(self, title) -> str:
        self.__title = title

    def get_id(self):
        return self.__id
    
    def get_title(self):
        return self.__title
    
    def isEqual(self, otherFilm):
        return otherFilm.get_id() == self.get_id()
    


    