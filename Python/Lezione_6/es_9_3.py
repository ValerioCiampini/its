class User:

    def __init__(self, name:str, lastname:str, password:str):
        self.name = name
        self.lastname = lastname
        self.password = password

    def describe_user(self):
        print(f"Name: {self.name}\nLastname: {self.lastname}\nPassword: {self.password}")

    def greet_user(self):
        print(f"Hello, {self.name}. Thanks for you subscrition")

u:User = User("a", "b", "c")
u1:User = User("e", "f", "g")

u.describe_user()
u.greet_user()

u1.describe_user()
u1.greet_user()