class Restaurant:

    def __init__(self, name:str, type:str, number_served:int = 0):
        self.name = name
        self.type = type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name} and is type is {self.type}, the number of customer have been served is {self.number_served}")

    def open_restaurant(self):
        print("The restaurant is open")

    def set_number_served(self, number_served):
        if number_served < 0:
            print("Errore")
        else:
            return number_served
        
    def increment_number_served(self):
        self.number_served += 1

r:Restaurant = Restaurant("a", "b", 3)
r.describe_restaurant()
r.increment_number_served()
r.describe_restaurant()
        
    