def sum(n:int):
    if n < 0:
        print("Error! Inserted number is negative!")
        return None

    else:
        somma:int = 0
        while n:
            somma += n
            n -= 1

        return int(somma)    
print(sum(5))