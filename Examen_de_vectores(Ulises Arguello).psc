Algoritmo Examen_vectores
	definir n Como Entero
	contM5=0
	Suma=0
	Escribir "�Bienvenido!"
	Escribir "Ingresa la cantidad de n�meros a evaluar: "
	leer n
	Para i <- 1 Hasta n Con Paso 1 Hacer
        Escribir "Ingrese el n�mero ", i, ":"
        Leer Num
        Si i = 1 Entonces
            mayor =Num
            menor =Num
        SiNo
            Si Num > mayor Entonces
                mayor =Num
            FinSi
            Si num < menor Entonces
                menor =Num
            FinSi
        FinSi
        Si Num > 5 Entonces
            contM5 = contM5 + 1
        FinSi
        Suma = Suma + Num
	FinPara
	Escribir "El n�mero mayor es: ", mayor
	Escribir "El n�mero menor es: ", menor
	Escribir "La cantidad de n�meros mayores que 5 es: ", contM5
	Escribir "La suma de todos los n�meros es: ", suma
	Escribir "Trabajo hecho por Ulises Arguello"
FinAlgoritmo
