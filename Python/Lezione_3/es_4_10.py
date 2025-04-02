#4-10  
nice_pizzas:list = ['Margherita', 'Diavola', 'Patate e Salsiccia', 'Quattro Formaggi', 'Capricciosa', 'Ortolana', 'Bianca']
first_three:list = nice_pizzas[:2 + 1]
print(f'The first three items in the list are {first_three}')
middle_three:list = nice_pizzas[3:5]
print(f'The middle two items in the list are {middle_three}')
last_three:list = nice_pizzas[5:]
print(f'The last two items in the list are {last_three}')