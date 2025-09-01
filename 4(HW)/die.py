"""9-13. Dice: Make a class Die with one attribute called sides, which has a
default value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll it 6 times."""

import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))

one = Die()
two = Die()
three = Die()
four = Die()
five = Die()
six = Die()

one.roll_die()
two.roll_die()
three.roll_die()
four.roll_die()
five.roll_die()
six.roll_die()

