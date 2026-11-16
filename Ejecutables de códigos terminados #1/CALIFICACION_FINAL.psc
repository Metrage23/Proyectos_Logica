//Calcula si un alUmno está aprobado o reprobado con base
//a su calificación.
Algoritmo CALIFICACION_FINAL
	Definir calificacion Como Real;
	calificacion <- 0;
	Escribir "Ingrese la calificación del alumno: ";
	Leer calificacion;
	SI (calificacion >= 3.5) Entonces
		Escribir "El alumno está APROBADO";
	SiNo
		Escribir "El alumno está REPROBADO";
	FinSi
FinAlgoritmo
