mySrtring = "Tierra mojada mis recuerdos de viaje, entre las lluvias"
print(mySrtring*3)
""" multi-line """
mySrtring = """                
                Tierra mojada
                mis recuerdos de viaje,
                entre las lluvias
                
                Mis pequeños peces blancos
                como si hirviera
                el color del agua
                """ 
print(mySrtring)


if "Tierra" in mySrtring:
    print("true")

print("agua" not in mySrtring)

print(mySrtring.__len__())

""" immutability - this brings an error because of immutability of item assignment"""
String = "texto"
String [0] = "T"