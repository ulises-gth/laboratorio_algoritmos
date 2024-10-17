nombres = [] #Crear una lista para almacenar los nombres

while True:
    nombre = input("Ingresa los nombres de los estudiantes por favor: \n"
                   "------------------------------------------------------\n"
                   "Utiliza 'FIN' para terminar la carga, y 'REPETIR' para ver los ya ingresados\n"
                   "------------------------------------------------------\n"
                   "Ingresa el nombre aquí: ").strip()

    nombre_a_lower = nombre.lower()  # Convierte el nombre a minúsculas

    if nombre_a_lower == "fin":  # Opción para finalizar el ingreso de nombres
        break

    elif nombre_a_lower == "repetir":  # Mostrar los nombres ingresados hasta ahora
       
        if nombres:
            print(f"Los nombres cargados son: {nombres}")
        else:
            print("No se han ingresado nombres aún.")
    
    elif nombre.isdigit():  # Validar si el nombre es un número o contiene numeros
        print("El nombre no puede ser un número.")
    
    elif nombre.strip() == "":  # Validar si el nombre está vacío(no contenga caracteres vacios)
        print("El nombre no puede estar vacío.")
    
    elif not nombre.replace(" ", "").isalpha(): # la funcion replace(remplaza los espacios en blanco de nombre con una cadena vacia,elimina todos los espacios en el nombre),
                                                # la funcion Isalpha(se aplica a la cadena y verifica que todos sean del alfabeto)
                                                # el not invierte e resultado de isalpha(para que sea verdadero)
        print("El nombre no puede contener caracteres especiales o números.")
    
    else:
        # Validamos cada parte del nombre
        partes = nombre.split() #el split divide la cadena en una lista de sub-cadenas(para ser verdadero)
        nombre_valido = True

        for parte in partes:
            if not parte.isalpha(): #Comprueba si esa parte contiene solo letras(sino no es valido)
                nombre_valido = False   #Si alguna parte contiene caracteres(el nombre se marca como no valido)
                break   #detiene el bucle si una parte no es valido
            
        if nombre_valido:
            nombres.append(nombre)
            print(f"Nombre '{nombre}' agregado correctamente.")
        else:
            print("El nombre contiene caracteres no alfabéticos.")
            
while True: #Menu de opciones para el usuario
    print("\nMenú de opciones:")
    print("1. Mostrar nombres ingresados")
    print("2. Ordenar los nombres alfabeticamente")
    print("3. Análisis de longitud de los nombres: Mostrar El nombre mas corto y largo")
    print("4. Contar vocales y consonantes en los nombres de manera combinada")
    print("5. Contar palabras en cada nombre")
    print("6. Inversión de los nombres")
    print("7. Mostrar solo los nombres que empiezan con una letra en particular")
    print("8. Buscar si un nombre está en la lista")
    print("9. Contar cuantos nombres contienen mas de 5 caracteres")
    print("10. Contar cuantos nombres contienen menos de 5 caracteres") #FUNCION AGREGADA
    print("11. Convertir todos los nombres con minusculas y mayusculas")
    print("12. Salir del programa")

    opcion = input("Elige una opción: ")
    
    if opcion == "1":   #Imprime todos los nombres con el orden que fueron ingresados
        print("Nombres ingresados:", nombres)

    elif opcion == "2": #ordena alfabeticamente los nombres en la lista
        nombres_minuscula=[nombre.lower() for nombre in nombres] #Se pasa a minuscula para evitar confunsion si agregan nombres con mayusucula
        nombres_ordenados = sorted(nombres_minuscula) #utiliza la funcion sorted para obtener una lista ordenada
        print("Los nombres ordenados alfabeticamente : ", nombres_ordenados)

    elif opcion == "3": #Encuentra y muestra el nombre mas largo y el mas corto en la lista
            
            nombre_mas_largo = max(nombres, key=len)    #usa MAX para obtener el nombre mas largo
            nombre_mas_corto = min(nombres, key=len)    #usa MIN para obtener el nombre mas corto 
            print(f"Nombre más largo es: {nombre_mas_largo}")
            print(f"Nombre más corto es: {nombre_mas_corto}")

    elif opcion == "4": #cuenta el total de vocales y consonantes en todos los nombres
        vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"    #Define las vocales como aeiou o AEIOU
        consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"#Define las consonantes sin contar espacios

        total_vocales = 0
        total_consonantes = 0

        for nombre in nombres:
            for letra in nombre:
                if letra in vocales:
                    total_vocales += 1
                else:
                    total_consonantes += 1
        print("Total de vocales:", total_vocales)
        print("Total de consonantes:", total_consonantes)

    elif opcion == "5":#Ciclo para contar palabras en cada nombre
        
        for nombre in nombres:
            contar_palabras=len(nombre.split())
            print(nombre,"Tiene",contar_palabras,"palabras")
        contar_palabras=sum(len(nombre.split())for nombre in nombres)
        print("El total de palabras son:",contar_palabras)   #usamos la funcion split para convertir una cadena en una sub-cadena
        
    elif opcion == "6":#Ciclo para invertir los nombres
        inversion_nombres=nombres[::-1]
        nombres_invertidos = [nombre[::-1] for nombre in nombres]

        print("Los nombres con el orden invertido : ",inversion_nombres)
        print("Nombres invertidos:", nombres_invertidos)

    elif opcion == "7":#Ciclo para buscar y mostrar nombres con una letra especifica(contando minusculas y mayusuclas)
        letra = input("Ingresa la letra a buscar: ").upper()
        nombres_con_letra = [nombre for nombre in nombres if nombre.upper().startswith(letra)]

        if nombres_con_letra:
            print(f"Los nombres que empiezan con '{letra}'Son: ", nombres_con_letra)
        else:
            print(f"No hay nombres que empiezan con '{letra}'.")

    elif opcion == "8":#Ciclo para buscar si un nombre esta en la lista(contando minusculas y mayusuclas)
        nombre_buscar = input("Ingresa el nombre a buscar: ").upper()
        nombres_upper=[nombre.upper() for nombre in nombres]

        if nombre_buscar in nombres_upper:
            print(f"El nombre '{nombre_buscar}' está en la lista.")
        else:
            print(f"El nombre '{nombre_buscar}' no está en la lista.")

    elif opcion == "9":#Ciclo para contar cuantos nombres tienen mas de 5 caracteres
        nombres_largos = [nombre for nombre in nombres if len(nombre) > 5]
        cont_nombres_largos = len(nombres_largos)

        if cont_nombres_largos > 0:
            print(f"Cantidad de nombres con más de 5 caracteres: {cont_nombres_largos}")
            print("Nombres:", nombres_largos)
        else:
            print("No hay nombres con más de 5 caracteres.")

    elif opcion == "10": #FUNCION AGREGADA
        nombres_cortos=[nombre for nombre in nombres if len(nombre) < 5]
        cont_nombres_cortos = len(nombres_cortos)

        if cont_nombres_cortos > 0:
            print(f"Cantidad de nombres con menos de 5 caracteres: {cont_nombres_cortos}")
            print("Nombres:",nombres_cortos )
        else:
            print("No hay nombres con menos de 5 caracteres.")
     
    elif opcion == "11":    #Ciclo para convertir todos los nombres a mayusculas y minusculas
        nombresconmayusculas = [nombre.upper() for nombre in nombres]
        nombresconminusculas = [nombre.lower() for nombre in nombres]

        print("Nombres en mayúsculas:", nombresconmayusculas)
        print("Nombres en minúsculas:", nombresconminusculas)

    elif opcion == "12":    #Ciclo para salir del programa
        print("-------------------------------------------------------------------")
        print("Saliendo del programa.")
        break

    else:
        print("Opción inválida. Por favor, elige una opción válida.")
