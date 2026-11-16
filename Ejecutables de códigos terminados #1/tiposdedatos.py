#Ejercicio 3
#Crear los siguientes tipos de variables, imprimirlas 
#y asignar su tipo:
#un entero, un flotante, cadena, caracter, booleano

talla= 32
print ("La talla es:", talla)
print ("La talla es un tipo de dato:", type(talla))

altura= 1.78
print ("La altura es:", altura)
print ("La altura es un tipo de dato:", type(altura))

nombre= "Julián"
print ("Mi nombre es:", nombre)
print ("El nombre es un tipo de dato:", type(nombre))

caracter= "$"
print ("El simbolo del dolar es:", caracter)
print ("El caracter es un tipo de dato:", type(caracter))

#booleano
tiene_licencia= True
tiene_casco= False

if tiene_licencia and tiene_casco:
    print("Puedes conducir la motocicleta sin problemas.")
else:
    print("No puedes conducir. Necesitas tanto la licencia como el casco.")
    print ("El booleano es un tipo de dato:", type(tiene_licencia))
