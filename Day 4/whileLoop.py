coins = 5

while coins > 0:
    coins = coins - 1
    print("You have " + str(coins) + " coin(s) left")
else:
    print('I dont have enough coins')


#while True:
    #pass # bassically do nothing but without an error


name = 'jose'
for letter in name:

    if letter == 'o':
     continue # ignoring letter o 

    print(letter)

    if letter == 's':
        print("I found letter " + letter)
        break


numero = 10
while numero >= 0:
    print(numero)
    numero -= 1
