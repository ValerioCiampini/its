def compoundInterest(m:int, t:int) -> float:
    if t == 0:
        return 0
    else:
        return float(m + compoundInterest(m * 1.005, t - 1))
    

print(compoundInterest(1000, 1))
        
