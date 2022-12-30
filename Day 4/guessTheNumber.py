from random import *

name = input('whats your name? ')
print(f'Well, {name}, im thinking  in a number from 1 to 100, and you only have 8 attempts to guess what is the number')

attempts = 0
opportunities = 8

randomNumber = randint(1, 101)

while True:
    number = int(input('writte your number (between 1 and 100)'))

    if opportunities == 0:
        
        opportunities = 8
        attempts = 0
        print(f"""your opportunities ended up \n \ni'll choose a new secrect number for you,
         now you have {opportunities} opportunities once again \n the old  secret number was {randomNumber} :D""" )
        randomNumber = randint(1, 101)

        continue

    if number < 1 or number > 100:
        print(f'your number isnt between 1 and 100 \n you still have {opportunities} opportunities')
        continue
    
    else:
        
        if randomNumber ==  number:
            opportunities -= 1 
            attempts += 1
            print(f'{name} congratulations you win in {attempts} attempts \n' )
            
            break

        if number < randomNumber:
            print(f'{name}, too low, you still have {opportunities} opportunities \n')
            opportunities -= 1 
            attempts += 1

        if number > randomNumber:
            print(f'{name}, too high, you still have {opportunities} opportunities \n')
            opportunities -= 1 
            attempts += 1