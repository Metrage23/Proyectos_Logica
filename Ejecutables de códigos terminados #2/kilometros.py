velocidad= int(input("Ingrese la velocidad actual: "))

if velocidad <= 30:
    print ("Zonas escolares")
elif velocidad <= 60:
    print ("Vías urbanas")
elif velocidad <= 80:
    print ("Vías rurales")
elif velocidad <= 100:
    print ("Rutas nacionales")
else:
    print ("Está por fuera de los límites de velocidad permitidos")
