myTuple = (1, 2, 3, 4, 2.21, False, 'text', "text")
myTuple2 = 1, 2, 3, 4

print(type(myTuple))
print(myTuple)
print(myTuple2)

""" tuples are immutable """

""" myTuple[0] = 0
print(myTuple) """ #Error


newTuple = 1, 4, 6, (23, 23, "31123", [1, 2, 3, [56]]), 324, "text"
print(newTuple[3][3][3], "getting values from a tuple")

""" list and tuples convertion """

#tuple to list
mylist = list(myTuple)
print(type(mylist))
print(mylist)

#list to tuple
myNewTaple = tuple(mylist)
print(type(myNewTaple))
print(myNewTaple)

""" variables to tuples - it also can be possible with list and dictionaries """
tuple = 1, 45, 23
x, y, z = 1, 2, 3

tuple = x, y, z 
print("x, y and z on a tuple", tuple)

""" tuple methods """
tuple = 1, 2, "tres", 4, 5, 6.0, 1, 1, 1, 2, 5, 23, 54


print(tuple.count(1))
print(tuple)


