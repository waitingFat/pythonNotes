import random


class Dice:
    def __init__(self):
        self.sides = 6
    def set_side(self,sides):
        self.sides = sides
    def roll(self):
        return random.randint(1,self.sides)

d = Dice()
d1 = Dice()

print d.roll()
print d1.roll()