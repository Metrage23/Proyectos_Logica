// Construir un pseudocódigo que permita ingresar
// un número, si el número es mayor de 500, se debe
// calcular y mostrar en pantalla el 18% de este.
Algoritmo porcentaje_del_numero
	Definir num, porcentaje Como Real
	Escribir 'Ingrese un numero: '
	Leer num
	Si num>500 Entonces
		porcentaje <- num*(18/100)
		Escribir 'El 18% es: ', porcentaje // 0.18
	FinSi
FinAlgoritmo
