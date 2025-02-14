#4-5
#using the one million list above (not repeating the for loop)
one_million:list = []
i:int = 1

while i < 1000000 + 1:
    one_million.append(i)
    print(one_million[i - 1])
    i += 1
    

a:int = min(one_million)
b:int = max(one_million)
c:int = sum(one_million)
print(a, b, c)
