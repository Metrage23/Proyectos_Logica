// Este ejercicio realiza el promedio de 4 materias.
//Imprime el promedio en pantalla
//y muestra un mensaje diferente si el promedio es mayor o menor que 4.5
Algoritmo prom 
	definir matematicas, castellano, ingles, sociales, promedio Como Real;
    imprimir ("ingrese la nota de matematicas: ");
	leer matematicas;
	imprimir ("ingrese la nota de castellano: ");
	leer castellano;
	imprimir ("ingrese la nota de ingles: ");
	leer ingles;
	imprimir ("ingrese la nota de sociales: ");
	leer sociales;
	promedio <- (matematicas+castellano+ingles+sociales)/4;
	Imprimir (promedio);
	si (promedio > 4.5) Entonces
		Imprimir ("Puedes acceder a la beca");
	SiNo
		Imprimir ("Aún no puedes acceder a la beca, intenta el otro semestre ");
	FinSi
FinAlgoritmo