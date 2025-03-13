n:int = int(input("inserisci un numero per vedere quanti numeri vuoi inserire: "))
somma:int = 0
media:float = 0
somma_p:int = 0
somma_d:int = 0

for i in range(n + 1):
    x:int = int(input("inserisci un numero: "))
    somma += x
    media = somma / i
    if x % 2 == 0 and x > media:
        somma_p += x
    elif x % 2 != 0 or x < media:
        somma_d += x
    
print(f"la somma dei pari è: {somma_p}\nla somma dei dispari: {somma_d}")
if somma_d > somma_p:
    print("la somma dispari è maggiore di quella pari")
else:
    print("la somma pari è maggiore di quella dispari")