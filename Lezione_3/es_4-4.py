#4-4
one_million:list = []
i:int = 1

while i < 1000000 + 1:
    one_million.append(i)
    print(one_million[i - 1])
    i += 1
    
