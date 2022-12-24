""" we cant change the type of value at any time """
data1 = 2
print(type(data1))
data1 = 2.2
print(type(data1))
data1 = True
print(type(data1))
data1 = "hi"
print(type(data1))


print(data1)


""" casting """

data = int(input("enter a number "))
print(type(data))
newValue = data + data 

print("new value " + str(newValue))

""" casting integers and floating points """
 
myInt = 5
myFloat = 2.8

r = int(myInt + myFloat)# just remains the left part of the number

print("new value "+ str(r))


var = True
print("boolean variable " + str(var))

""" casting - adding strings """
num1 = "20"
num2 = "2.4"

num1I = int(num1)
num2f = float(num2)

print(num1I + num2f)
