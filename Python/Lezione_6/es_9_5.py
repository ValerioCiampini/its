class User:

    def __init__(self, name:str, lastname:str, password:str):
        self.name = name
        self.lastname = lastname
        self.password = password
        self.login_attemps = 0

    def describe_user(self):
        print(f"Name: {self.name}\nLastname: {self.lastname}\nPassword: {self.password}")

    def greet_user(self):
        print(f"Hello, {self.name}. Thanks for you subscrition")

    def increment_login_attempts(self):
        self.login_attemps += 1
    
    def reset_login_attempts(self):
        self.login_attemps = 0

u:User = User("a", "b", "c")
u.increment_login_attempts()
u.increment_login_attempts()
print(u.login_attemps)
u.reset_login_attempts()
print(u.login_attemps)