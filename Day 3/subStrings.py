text = "this is some random text"

print(text[0 : 3 + 1])
print(text[0 : 4])
print(text[0 : text.__len__() : 2])
print(text[0 : ])
print(text[0 : : 2])

frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"

print(frase[::-1])# invertido

print("".join(reversed(frase)))

""" print(frase[0: : -1]) """