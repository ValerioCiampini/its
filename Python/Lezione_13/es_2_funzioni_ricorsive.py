def compoundInterest(m:int, t:int) -> int:
    if t == 0:
        return 0
    else:
        return m + compoundInterest(m * 1005, t - 1)
    

print(compoundInterest(1, 4))
        
