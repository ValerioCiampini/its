nice_pizzas:list = ['Margherita', 'Diavola', 'Patate e Salsiccia', 'Quattro Formaggi', 'Capricciosa', 'Ortolana', 'Bianca']
friend_pizzas:list = nice_pizzas[:]
nice_pizzas.append('Vegetariana')
friend_pizzas.append('Quattro Stagioni')
for my_pizzas in nice_pizzas:
    print(f'My favorite pizzas are {my_pizzas}')
    
for friend_favorite in friend_pizzas:
    print(f'My friends favorite pizzas are {friend_favorite}')