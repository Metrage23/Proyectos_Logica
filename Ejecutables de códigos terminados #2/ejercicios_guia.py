"""
INTRODUCCIÓN AL DESARROLLO DE SOFTWARE
Guía de Estudio: Métodos de str en Python
Ejemplos de los métodos más utilizados de la clase str
"""


# 1. len() — Longitud de la cadena
 
print("1. len() — Longitud de la cadena")
texto = "Python"
print(len(texto))

print()

 
# 2. .upper() — Convierte a mayúsculas
 
print("2. .upper() — Convierte a mayúsculas")
palabra = "python"
print(palabra.upper())

print()

 
# 3. .lower() — Convierte a minúsculas

print("3. .lower() — Convierte a minúsculas")
palabra = "PYTHON"
print(palabra.lower())

print()

 
# 4. Indexación [ ] — Carácter en una posición

print("4. Indexación [ ] — Carácter en una posición")
texto = "Hola"
print(texto[1])

print(texto[-1]) 

print()

 
# 5. Slicing [ : ] — Extraer subcadena

print("5. Slicing [ : ] — Extraer subcadena")
palabra = "Programacion"
print(palabra[0:7])

print()

 
# 6. == — Comparar cadenas (distingue mayúsculas y minúsculas)
 
print("6. == — Comparar cadenas")
a = "Python"
b = "python"
print(a == b)

print()


# 7. .lower() — Comparar ignorando mayúsculas

print("7. .lower() — Comparar ignorando mayúsculas")
a = "Python"
b = "python"
print(a.lower() == b.lower())

print()

 
# 8. in — Verificar si contiene una subcadena

print("8. in — Verificar si contiene una subcadena")
frase = "Aprender Python es divertido"
print("Python" in frase)

print()

 
# 9. .replace() — Reemplazar caracteres o subcadenas

print("9. .replace() — Reemplazar caracteres o subcadenas")
palabra = "casa"
print(palabra.replace("a", "o"))

print()


# 10. .strip() — Eliminar espacios al inicio y al final

print("10. .strip() — Eliminar espacios al inicio y al final")
texto = "  Hola Python  "
print(texto.strip())
