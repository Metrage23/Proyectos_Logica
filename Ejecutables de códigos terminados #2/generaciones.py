año= int(input("Ingrese año de nacimiento: "))

if año >= 1994 and año <= 2010:
    print("Eres de la generacion Z")
elif año >= 1981 and año <= 1993:
    print("Eres Millennial")
else:
    print("Eres de otra generacion")