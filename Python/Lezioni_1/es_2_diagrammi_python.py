import math

max:int = int(input("inserisci il max: "))
i:int = 0

while i < 4:
    i += 1
    n:int = int(input("inserisci un numero: "))

    if n > max:
        max = n
    
print(max)

max:int = int(input("inserisci il max: "))
i:int = 0

while True:
    if i == 4:
        break
    else:
        i += 1
        n:int = int(input("inserisci un  numero: "))

        if n > max:
            max = n

print(max)

max:int = int(input("inserisci il max: "))

for j in range(4):
    n:int = int(input("inserisci un numero: "))

    if n > max:
        max = n

print(max)