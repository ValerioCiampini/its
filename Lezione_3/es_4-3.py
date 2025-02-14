#4-3

counter:list = []
i:int = 1
n:int = int(input("inserisci un numero da raggiungere: "))

while i < n + 1:
    counter.append(i)
    print(counter[i - 1])
    i += 1
    