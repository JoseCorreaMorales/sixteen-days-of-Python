#from random import randint

from random import *

rand =  randint(0, 10000)
print(rand) 

unfRand = uniform(0, 10000)
unfRandRound = round(uniform(0, 10000), 1)
print(unfRand)
print(unfRandRound)

""" numbers between 0 and 1 """
CeroOne = random()
print(CeroOne)

colors =['blue', 'green', 'yellow', 'orange', 'orange', 'red', 'green']
color = choice(colors)
print(color)


numbers = []

for i in range(100):
    numbers.append(randint(0, 100))

#print(numbers)

mynumbers = list(range(100))
shuffle(mynumbers)
print(mynumbers)