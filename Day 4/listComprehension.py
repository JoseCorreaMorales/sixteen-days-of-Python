word = 'python'

listLetters = []

for letter in word:
    listLetters.append(letter)
print(listLetters)



""" in a comprehensive manner would look like"""
myList = [letter for letter in word]
print(myList) 


number = [number for number in range(10)]
print(number)




""" list comprehension """
""" limit = int(input('what is the limit? '))

pairNumbers = [number for number in range(0, limit + 1, 2)]
print(pairNumbers) """


""" modifiding the result before including in the list """
numbersList = [(number * 2 + 5)- 1 for number in range(11)]
print(numbersList)


""" list comprehension with if statement """
numbers = [number for number in range(0, 11) if number % 2 == 0 or number == 3]
print(numbers)



""" list comprehension with if-else statement """
test = [number if number % 5 == 0 else f'{number} isnt  divisible by 5'  for number in range(0, 11)]
print(test)

""" feets to meters conversion """
feets = [20, 42, 100, 1000, 5000, 10000, 21, 23, 21, 1]

meters = [round(f * 3.281, 2) for f in feets]
print(meters)


"""  """
fahrenheit = [32, 212, 275]

celsius = [(f - 32) * (5/9) for f in fahrenheit]

