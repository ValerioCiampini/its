import random

class Dice:

    def __init__(self, sides:int = 6):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))


d:Dice = Dice()
d.roll_die()
d1:Dice = Dice(20)
d1.roll_die()