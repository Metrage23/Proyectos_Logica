// Elaborar un algoritmo que permita ingresar el
// nombre del trabajador, su sueldo básico y el
// número de hijos, se deberá mostrar su
// bonificación y el sueldo final. Tenga en cuenta
// que la empresa está dando una bonificación
// del 7 MOD  del sueldo básico sólo si el trabajador tuviese hijos
Algoritmo bonificacion_total
	Definir nombre Como Cadena
	Definir basico Como Real // Entrada
	Definir hijos Como Entero // Entrada
	Definir bonificacion, final Como Real // Entrada
	Escribir 'Ingrese el nombre del trabajador: ' // Salida
	Leer nombre
	Escribir 'Ingrese el sueldo basico: '
	Leer basico
	Escribir 'Ingrese el numero de hijos: '
	Leer hijos
	bonificacion <- 0
	Si hijos>0 Entonces
		// se multiplica el básico, por el 7 MOD , por los hijos
		bonificacion <- basico*0.07*hijos
	FinSi
	final <- basico+bonificacion
	Escribir 'La bonificacion es de : ', bonificacion
	Escribir 'El sueldo final es de : ', final
FinAlgoritmo
