"""9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters.
Randomly select 4 numbers or letters from the list and print a message saying that
any ticket matching these 4 numbers or letters wins a prize."""

import random

list_of_numbers = ['a', 'b', 'c', 'd', 'e']
win = ''

for i in range(10):
    list_of_numbers.append(i)

for i in range(4):
    choice =random.choice(list_of_numbers)
    win += str(choice)

# print(f"Winner's ticket is {win}.")



"""9-15. Lottery Analysis: You can use a loop to see how hard it might be to win
the kind of lottery you just modeled. Make a list or tuple called my_tickets. Write
a loop that keeps pulling numbers until your ticket wins. Print a message report-
ing how many times the loop had to run to give you a winning ticket."""

my_tickets = []
ticket = 'a542'


while True:
    win = ''
    for i in range(4):
        choice = random.choice(list_of_numbers)
        win += str(choice)
        my_tickets.append(win)

    if ticket == win:
        print(f"I win! Before that I bought ticket: {len(my_tickets)} times")
        break


