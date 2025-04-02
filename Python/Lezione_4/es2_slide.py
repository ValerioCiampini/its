def check_lenght(string:str):
    if len(string) > 10:
        print(f"{string} is bigger than 10")
    elif len(string) < 10:
        print(f"{string} is smaller than 10")
    else:
        print(f"{string} is equal to 10")

check_lenght("Hello world!")