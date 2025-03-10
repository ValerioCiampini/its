#4-2

animals:list = ['Dog', 'Cat', 'Parrot']
i:int = 0

while i < len(animals):
    print(f'A {animals[i]} would make a great pet')
    i += 1
    
print(f'A {animals[0]}, a {animals[1]} and {animals[2]}, have in common the fact that they are domestic animals.\n But they all are great pets!')
