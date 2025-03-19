def countdown(n:int) -> None:
    if n < 0:
        return print("Error. the number must be positive")
    
    while n >= 0:
        print(n)
        n -= 1

countdown(-5)
countdown(5)