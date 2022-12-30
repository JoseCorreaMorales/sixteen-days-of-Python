minValue = min(123, 34, 342,213,22, 42, 1)
maxValue = max(123, 34, 342,213,22, 42, 1)
print(minValue, maxValue)

numbers = [342, 43534, 2323, 6403, 232, 32]
print(min(numbers), max(numbers))

words = ['april', 'may', 'january', 'aug', 'september', 'oct', 'nov']
print(min(words), max(words))

name = 'jose'
print(min(name.lower()),  max(name.lower()))

mydict = {'key 1': 1, 'key 2': 2, 'key 3': 3}
print(min(mydict), max(mydict))
print(min(mydict.values()), max(mydict.values()))