class Persona:

    def __init__(self, name:str, last_name:str):

        if isinstance(name, str) == False: 
            self.__name = None
            raise ValueError("Il nome inserito non è una stringa!")
        else:
            self.set_name(name)
        
        if isinstance(last_name, str) == False:
            self.__name = None
            raise ValueError("Il cognome inserito non è una stringa!")
        else:
            self.set_last_name(last_name)

        if isinstance(last_name, str) == True and isinstance(name, str) == True:
            self.__eta = 0
        else:
            self.__eta = None

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise ValueError("Il nome inserito non è una stringa!")
        
    def set_last_name(self, last_name):
        if isinstance(last_name, str):
            self.__last_name = last_name
        else:
            raise ValueError("Il cognome inserito non è una stringa!")
        
    def set_age(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            raise ValueError("L'età inserito non è una stringa!")
        
    def get_name(self):
        return self.__name
    
    def get_last_name(self):
        return self.__last_name
    
    def get_age(self):
        return self.__age
    
    def greet(self):
        print(f"Ciao, sono {self.__name} {self.__last_name}! Ho {self.__age} anni!")

