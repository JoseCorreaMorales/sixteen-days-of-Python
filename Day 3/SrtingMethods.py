text = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
text2 = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
print(text.upper() +"\n" 
+ text.lower() + "\n" +
text[0].lower() + "\n"
)

print(text.split())
print(text.split("t"))

a = "Learn"
b = "Python"
c = "its pretty cool"
c = "-".join([a, b, c])
print(c)

print(text2.find("cool")) #iif find doesn't find the given parameter then return -1, instead of an
# error (witchs is what happen with index())


var = text2.replace("is", "IS")
print(var)

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
nuevaFrase = frase.replace("difícil", "fácil").replace("mala", "buena")
print(nuevaFrase)
