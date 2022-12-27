aSet = set([1, 2, 3, 4, 5, 5.0])
print(type(aSet), aSet)

""" union """
mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5} 

mi_set3 = mi_set_1.union(mi_set_2)

aSet = {1, 2, 3, 4, 5, 1.0, "red"}
print(type(aSet))

""" set elements can not have repeated elements, list or dictionaries inside, assign elements
 or even access to a certain index BUT sets can accept tuples because tuples are also immutables
 """
mySet = set([1, 2, 3, 4, 5, 1, 2])
""" print(mySet) #error
print(mySet[0]) #error
mySet[0] = 100 # error """
print(mySet)

myset1 = {1, 2, 3, (4, 5, 6, 7, 1, 1, 2, 2, 5), 1, 1, 1, 2, 2, 5} #correct
print(myset1)
""" Set() methods """

myset1.add(99)
print(myset1, "99 now added")
myset1.remove(1)
print(myset1)
myset1.remove(9999) #if i try to eliminate a nonexistent elements an error shows

myset1.pop() # if i don't specify a parameter inside the method then pop() is
# gonna delete a random number because the sets are a unordered structure

myset1.clear() #deletes everything