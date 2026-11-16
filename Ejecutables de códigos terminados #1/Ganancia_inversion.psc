//Una persona desea invertir su capital en un banco y desea saber 
//cuánto dinero ganará después de un mes si el banco le pagará intereses del 2% mensual
//Cree un algoritmo para solucionarlo.
	Algoritmo Ganancia_inversion
		DEFINIR interes Como Real;
		DEFINIR dias, capital, ganancia Como Entero;
		ESCRIBIR "Ingrese el monto a invertir: ";
		LEER capital;
		ESCRIBIR "Ingrese el número total de días del mes a considerar: ";
		LEER dias;
		interes <- 0.02;
		ganancia <- (capital * dias) * interes;
		ESCRIBIR "La ganancia por cobrar después del mes es de: ";
		ESCRIBIR ganancia;
	FinAlgoritmo