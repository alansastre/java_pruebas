Funcion mayorEdad <- CalculoEdad ( edad )
	mayorEdad <- edad >= 18
Fin Funcion

Funcion saludoPersona ( nombre, apellido )
	Escribir "Bienvenido a PseInt: " nombre," " apellido
	
Fin Funcion

Algoritmo Funciones_propias
	Escribir "ingresa tu edad: "
	leer edad
	
	
	Si mayorEdad Entonces
		Escribir "Eres mayor edad"
	SiNo
		Escribir "Eres menor de edad"
	Fin Si
	
	
	nombre <- "Carlos"
	apellido <- "Feliz"
	saludoPersona(nombre, apellido)
	saludoPersona(nombre, apellido)
	saludoPersona(nombre, apellido)
	
FinAlgoritmo
