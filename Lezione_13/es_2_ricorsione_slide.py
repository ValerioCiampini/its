def sum(n:int):
    if n < 0:
        print("Error")
        return None
    
    elif n == 0:
        return 0

    else:
        n = n + sum(n-1)
        return n

print(sum(5))

    
