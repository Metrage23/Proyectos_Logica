// Escriba un algoritmo que le permita obtener la cantidad 
// de arena necesaria para revocar una pared cualquiera
// según sus medidas (largo y alto) expresadas en metros.
Algoritmo CANT_ARENA
	DEFINIR metros, arena, largo, ancho Como Real;
			metros <- 0.5;
			ESCRIBIR "Ingrese el largo de la pared en metros: ";
			LEER largo;
			ESCRIBIR "Ingrese el ancho de la pared en metros: "; 
			LEER ancho;
			arena <- (largo * ancho) * metros;
			ESCRIBIR "La cantidad de arena necesaria es de: ";
			ESCRIBIR arena;
FinAlgoritmo