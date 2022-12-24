name = input("Cual es tu nombre?")
venta = input("Cuanto vendiste?")

ventaI = float(venta)

comisiones = (ventaI * 13)/100


print("{} tus comisiones de este mes son: {}".format(name, round(comisiones, 2)))