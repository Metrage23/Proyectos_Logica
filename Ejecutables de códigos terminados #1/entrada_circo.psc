	//La entrada a un circo vale 10.000 por persona,
	//sin embargo, si la edad de la persona es menor
	//de 10 años se le da un descuento del 25% en el
	//valor del boleto. Escribir el seudocódigo que
	//calcule y muestre lo que pagará por la entrada
	//al circo según la edad.
	//Declaracion de Variables
Algoritmo entrada_circo
	Definir precio como Real;
	Definir edad como Entero;
	//Entradas
	Escribir "Ingrese el precio de la entrada: ";
	Leer precio
	Escribir "Ingrese la edad del cliente: ";
	Leer edad
	//Proceso
	Si edad < 10 Entonces
		precio <- precio - (precio * 0.25)
	FinSi
	Escribir "El monto final a pagar es: ", precio;
FinAlgoritmo