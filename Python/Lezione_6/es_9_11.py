class User:

    def __init__(self, name:str, lastname:str, username:str, email:str):
        self.name = name
        self.lastname = lastname
        self.username = username
        self.email = email 

    def describe_user(self):
        print(f"Name: {self.name}\nLastname: {self.lastname}\nUsername: {self.username}\nEmail: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.name}. Thanks for you subscrition")

class Privileges:
    
    def __init__(self):
        self.privileges = []

    def show_privileges(self):
        return self.privileges
    
class Admin:
    def __init__(self, user:User, privileges:Privileges):
        self.user = user
        self.privileges = privileges
        

