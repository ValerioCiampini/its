class Restaurant:

    def __init__(self, name:str, type:str):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name} and is type is {self.type}")

    def open_restaurant(self):
        print("The restaurant is open")


r:Restaurant = Restaurant("a", "b")
r.describe_restaurant()
r.open_restaurant()