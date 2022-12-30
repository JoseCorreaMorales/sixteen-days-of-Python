list = ['Jose', 'Jue', 'Mira', 'Amin', 'Er']

for i in list:
   print("Hello " + i, list.index(i))


word = 'Hello'
for letter in word:
    print(letter, word.index(letter))

index = 0
for i in list:
    if i.startswith('L') and i.endswith('s'):
        print("code")
    if i[index] == 'J':
        print('the name ', i, "have the letter ", i[index])
index += 1



numbers = [1, 2, 3 ,4, 5]
result = 0
for i in numbers:
    result += i 

print(result)

""" objects """
for i in [[1, 2,[99, 100], [9999, 00000], {'key 1': 1}],[3, 4],[5, 6]]:
    print(i)


dict = {"key 1": 1, "key 2": 2, "key 3": 3}
for i in dict:
    print(i, dict[i])

for i in dict.items():
    print(i)