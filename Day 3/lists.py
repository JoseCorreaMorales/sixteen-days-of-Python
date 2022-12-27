firtsList = ['a', 'b', 'c', 'd'] 
secList = ['e', 'f', 'g', 'h']
thridList = firtsList + secList
print(type(firtsList))
print(firtsList + secList)
print(thridList)
print(thridList[-1])


""" adding elements """
thridList.append("i")
print(thridList)

thridList.insert(0, "Frist element")
print(thridList)

thridList.pop(0)
print(thridList)

deletedItem = thridList.pop(0)
thridList.append(deletedItem)
print(thridList)

""" sorting """
newList = [1, 4, 6, 2, 20, 4, 32, 5223]
newList.sort()
print(newList) #this works but the internal structure of the list doesnt change, so the sort() method doesnt return anything
# that why i cant assign the ordered list to a variable 

orderedList = newList.sort()
print(orderedList)# error


""" this works but now i get something redundant, cus now a have two identical lists """
myList = [1, 5, 2, 54, 123, 3, 75, 23, 12, 99]
myList.sort()
myOrderedList = myList
print(myOrderedList)
print(myList)

""" reverse list """
myOrderedList.reverse()
print(myOrderedList)