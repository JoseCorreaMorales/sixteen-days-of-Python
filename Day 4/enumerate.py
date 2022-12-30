mylist = [1,2 ,3,4,5,6,7,8,9]

for i in enumerate(mylist):
   print(i)
   print(type(i), '\n')

for index, item in enumerate(mylist):
   print(index, item, '\n')


for index, item in enumerate(range(20, 31)):
    print(index, item, '\n')

for i, item in enumerate(range(50, 58)):
    print(i, item ,'\n')

#nop
""" for i, item in mylist:
    print(item) """


""" mylist to tuple """
myTuples = enumerate(mylist)
print(myTuples)
print(type(myTuples), '\n')

""" casting tuple """
myTuple = list(enumerate(mylist))
print(myTuple)
print(type(myTuple), '\n')

""" ex """
names_list = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]


for index, name in enumerate(names_list):
    print(f'{name} are in index No. {index}')


word = "Python"

index_list= list(enumerate(word))
print(index_list)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for index, item in enumerate(lista_nombres):
    if item.startswith('M'):
        print(index)