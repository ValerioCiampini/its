#1-1
x:float = 4.25
y:float = (1.0/x)

print(f"Il valore di x è:{x}\nIl valore di y è: {y:.2f}\nIl prodotto tra x e y è: {x*y}")
print(x-(x*y))


#1-2
x:float = 4.25
y:float = (x%2.0)

print(f"Il valora di x è:{x}\nIl valore di y è:{y:.2f}")

x2:float = -4.25
y2:float = (x2%2.0)

print(f"Il valore di x è:{x2}\nIl valore di y è:{y2:.2f}")


#1-3
x:int = 3
y:int = 5
z:int = 7

print(f"La media tra x, y e z è:{(x+y+z)/3}")


#1-4
x:int = 2024

print(f"La prima cifra è: {x-2022}")
print(f"La seconda cifra è: {x-2024}")
print(f"La terza cifra è: {x-2022}")
print(f"La quarta cifra è: {x-2020}")


#1-5
gradi_Fahrenheit:int = 97
gradi_Celsius:float = 5*(gradi_Fahrenheit-32)/9

print(f"{gradi_Fahrenheit} gradi Fahrenheit corrispondono a {float(gradi_Celsius):.1f} gradi Celsius")

#1-6
ordine:dict = { "Pasta":10.50, "Hamburger":15.50, "Verdura":7, "Acqua":1.50, "Tiramisu":6 }
totale:float = (10.50 + 15.50 + 7 + 1.50 + 6)
print(f"Il totale sarà:{totale}")

#2-3
friend:str = "Luke"
print(f"Hello {friend}, would you like to learn some python today?")
#2-4
homie:str = "casti"
print(homie.upper())
print(homie.lower())
print(homie.title())
#2-5
print("George Washington once said, \"To be prepared for war is one of the most effective means of preserving peace.\"")
#2-6
famous_person:str = "George Washington"
print(f"{famous_person} once said, \"To be prepared for war is one of the most effective means of preserving peace.\"")
#3-1
My_friends:list = ["Luca", "Federico", "Casti", "Giacomo"]
print(My_friends[0])
print(My_friends[1])
print(My_friends[2])
print(My_friends[3])
#3-2
print(f"Hey {My_friends[0]}, how are you doing today")
print(f"Hey {My_friends[1]}, how are you doing today")
print(f"Hey {My_friends[2]}, how are you doing today")
print(f"Hey {My_friends[3]}, how are you doing today")
#3-3
cool_ways_to_ride:list = ["Honda Cbr 600", "Gt86", "Porsche Gt3rs"]
print(f"If I need to choose between my favourite mode of transportation I would say that driving a {cool_ways_to_ride[0]} would be cool")
print(f"However, if it's rainy I would like to drive a {cool_ways_to_ride[1]}; even a {cool_ways_to_ride[2]} would not be bad")

#3-4
people_for_dinner:list =  ["Einstein", "Da Vinci", "Napoleone"]
for people in people_for_dinner:
    print (f'Hello {people} I would like to invite you to dinner')

#3-5
people_for_dinner:list =  ["Einstein", "Da Vinci", "Napoleone"]
print(f"Sorry about the fact that tonight you will not be join us {people_for_dinner[2]}")
people_for_dinner.pop(2)
people_for_dinner.insert(2, "Lebron")
for people in people_for_dinner:
    print (f'Hello {people} I would like to invite you to dinner')
#3-6
people_for_dinner:list =  ["Einstein", "Da Vinci", "Napoleone"]
print(f"Good evening, {people_for_dinner[0]}, {people_for_dinner[1]}, {people_for_dinner[2]}. I have found a bigger dinner table for tonight")
people_for_dinner.insert(0, "Lincoln")
people_for_dinner.insert(1, "Curry")
people_for_dinner.append("Tom Brady")
for people in people_for_dinner:
    print (f'Hello {people} I would like to invite you to dinner')
#3-7
people_for_dinner:list =  ["Einstein", "Da Vinci", "Napoleone"]
print(f"Good evening, {people_for_dinner[0]}, {people_for_dinner[1]}, {people_for_dinner[2]}. I have found a bigger dinner table for tonight")
people_for_dinner.insert(0, "Lincoln")
people_for_dinner.insert(1, "Curry")
people_for_dinner.append("Tom Brady")
for people in people_for_dinner:
    print (f'Hello {people} I would like to invite you to dinner')

print("Unfortunately I just received the message that the table will not be shipped in time for tonight.\nTherefore I will be able to invite only to people for dinner")


while len(people_for_dinner) > 2:
    removed_guests = people_for_dinner.pop()
    print(f'Sorry {removed_guests} you cannot come')

for people in people_for_dinner:
    print (f'Hello {people} I would like to invite you to dinner')

del people_for_dinner[0]
del people_for_dinner[0]

#3-8
cool_places:list = ["Austria", "Usa", "Germany", "Japan", "Ireland"]
print(*cool_places)
cool_places_sorted:str = sorted(cool_places)
print(*cool_places_sorted)
print(*cool_places)
cool_places_sorted_backwards:str = sorted (cool_places, reverse=True)
print(*cool_places_sorted_backwards)
print(*cool_places)
cool_places.reverse()
print(*cool_places)
cool_places.reverse()
print(*cool_places)
cool_places.sort()
print(*cool_places)
cool_places.sort(reverse=True)
print(*cool_places)

#6-1
info:dict = {"name":"Marco", "last_name":"Rossi", "age":20, "city":"Roma"}

for key, value in info.items():
    print(value)

#6-2
favourite_numbers:dict = {"Erik":20, "Marie":12, "James":7}

for key, value in favourite_numbers.items():
    print(f"Hi, my name is {key} and my favourite number is: {value}")
