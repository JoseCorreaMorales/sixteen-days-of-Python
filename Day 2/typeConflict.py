age = input("How old are u?")

print("U are " + age + " years old")

#all the things that we get from an input will be always a string:
print(type(age))

# so this is wrong
newAge = age + 1 #we cant concatenate a str and int
print("next year u will be " + newAge)



number = input("tell me a number ")

print(number + number) #the result will be concatenated instead of adding it
