def suminRange(a:int, b:int) -> int:
    if a > b:
        i:int = a
        a = b
        b = i
    
    somma:int = 0
    while a <= b:
        somma += a
        a += 1
        
    return int(somma)
    
print(suminRange(10, 5))