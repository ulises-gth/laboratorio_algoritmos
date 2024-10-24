Algoritmo Examen_Matriz
	
	Definir cantidad_fruta, matrizfrutas,nombrearticulo , fruta_buscada Como Caracter
	Definir indice Como Entero
	Dimension matrizfrutas[5,2]  
	cantidad_fruta = ""
	fruta = ""
	indice = 1
	Escribir "¡Bienvenido al programa!"
	Escribir "1.*Para Ingresar una fruta"
	Escribir "2.*Para buscar una fruta" 
	Escribir "3.*Mostrar las frutas que fueron ingresadas"
	Escribir "4.*Salir del programa."
	Leer opcion
	Mientras opcion <> 4 Hacer
		
		Si opcion = 1 Entonces
			Si indice <= 5 Entonces
				Escribir "Ingresa el nombre de la fruta: "
				Leer fruta
				fruta = Minusculas(fruta)
				matrizfrutas[indice,1] = fruta
				Escribir "Ingresa la cantidad: "
				Leer cantidad_fruta
				matrizfrutas[indice,2] = cantidad_fruta
				indice = indice + 1
			SiNo
				Escribir "No se pueden ingresar más frutas."
			FinSi
		FinSi
		
		Si opcion = 2 Entonces
			Escribir "Ingrese el nombre de la fruta a buscar:"
			Leer fruta_buscada
			fruta_buscada = Minusculas(fruta_buscada)
			encontrado = Falso
			Para i Desde 1 Hasta indice - 1 Hacer
				Si matrizFrutas[i,1] = fruta_buscada Entonces
					Escribir "Aquí está la fruta que buscabas:", matrizfrutas[i,1]
					Escribir "Su cantidad es:", matrizfrutas[i,2]
					encontrado = Verdadero
				FinSi
			FinPara
			SI No encontrado Entonces
				Escribir "Fruta no encontrada"
			FinSi
		FinSi
		
		Si opcion = 3 Entonces
			Escribir "Frutas ingresadas:"
			Para i Desde 1 Hasta indice - 1 Hacer
				Escribir "Fruta: ", matrizfrutas[i,1]
				Escribir "Cantidad: ", matrizfrutas[i,2]
			FinPara
		FinSi
		

		SI No (opcion = 1 O opcion = 2 O opcion = 3) Entonces
			Escribir "Opción incorrecta.Por favor ingrese una opción  que sea valida."
		FinSi
		Escribir "1.*Para Ingresar una fruta"
		Escribir "2.*Para buscar una fruta" 
		Escribir "3.*Mostrar las frutas que fueron ingresadas"
		Escribir "4.*Salir del programa."
		Leer opcion
	FinMientras
	Escribir  "Trabajo hecho por Ulises Arguello"
FinAlgoritmo