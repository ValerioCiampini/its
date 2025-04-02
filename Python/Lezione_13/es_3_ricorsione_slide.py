def suminRange(a:int, b:int) -> int:
    if a > b:
        a, b = b, a
    
    elif a == b:
        return a
    
    a = a + suminRange(a + 1, b)
    return int(a)
    
print(suminRange(10, 5))