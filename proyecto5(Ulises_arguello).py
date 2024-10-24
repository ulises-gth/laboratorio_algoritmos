import random

# Lista de palabras posibles
palabras = ["matematica", "jirafa", "heladera", "perro", "secreto"]

# Función para elegir una palabra secreta al azar
def elegir_palabra():
    return random.choice(palabras)

# Función para pedir al jugador una letra
def pedir_letra():
    letra = input("Elige una letra: ").lower()
    while not letra.isalpha() or len(letra) != 1:   #un ciclo verdadero que verifica que la entrada tenga la longitud de un caracter y este en el alfabeto
        letra = input("Por favor, elige una letra válida: ").lower()    #si la entrada no cumple ambas condiciones, de lo contrario ingrese una letra valida
    return letra

# Función que toma 4 parametros(letra que ingreso el jugador,la palabra que el jugador trata de adivinar,las letras que adivino y las vidas)
def verificar_letra(letra, palabra_secreta, letras_adivinadas, vidas):  #esta funcion toma 4 parametros
    if letra in palabra_secreta:    #ciclo para verificar si la letra esta en la palabra secreta
        print("¡Bien hecho! La letra está en la palabra.")  
        for i, caracter in enumerate(palabra_secreta):  #ciclo para verificar si la letra esta en la palabra secreta y cuando encuentra una coincidencia con la letra
            if caracter == letra:
                letras_adivinadas[i] = letra  #actualiza la lista
                
    else:
        if letra not in letras_adivinadas:
            print("La letra no está en la palabra.")
            vidas -= 1  
    return letras_adivinadas, vidas

# Función que verifica si el usuario gano o no gano
def verificar_ganador(letras_adivinadas):
    return "_" not in letras_adivinadas

# Función para mostrar el menú y preguntar si el usuario quiere seguir jugando o quiere abandonar el programa
def mostrar_menu():
    while True:
        respuesta = input("\n¿Quieres seguir jugando? (si/no): ").lower()
        if respuesta == 'si':
            jugar_ahorcado()
        elif respuesta == 'no':
            print("Gracias por jugar. ¡Hasta luego!")
            dibujo = """
              .--.
           __/o    \\
       _ /       () \\
     .' \\|   __  \\   |
    /    \\_/|  \\   \\ /
   / / /|/  \\__/    /
  \\__/             /
      \\    .       \\
        \\     Y     \\
          \\  |   |   |
           `"|   |   |
             |   |   |
             |   |   |
             |   |   |
             |___|___|
            `"`"``'"'"`
        """
            print(dibujo)
            break
        else:
            print("Por favor, elige una opción válida: 'si' para seguir jugando o 'no' para finalizar.")

# Función principal del juego
def jugar_ahorcado():
    palabra_secreta = elegir_palabra()
    vidas = 6
    letras_adivinadas = ["_"] * len(palabra_secreta)

    print("¡Bienvenido al juego del ahorcado!")
    print(" ".join(letras_adivinadas))  #convierte la lista en una cadena separada por espacios

    #ciclo para que el jugador siga jugando mientras tenga vidas.
    while vidas > 0 and not verificar_ganador(letras_adivinadas):
        letra = pedir_letra()   #pide una letra
        letras_adivinadas, vidas = verificar_letra(letra, palabra_secreta, letras_adivinadas, vidas)    #verifica la letra y actualiza el estado del juego y se asignan los valores actualizados a las mismas
        print(" ".join(letras_adivinadas))  #Muestra el estado actual de las letras y convierte la lista en una cadena separada por espacios
        print(f"Vidas restantes: {vidas}")

    if verificar_ganador(letras_adivinadas):
        print("\n¡Felicidades! Has adivinado la palabra:", palabra_secreta)
    else:
        print("\nTe has quedado sin vidas. La palabra era:", palabra_secreta)

    mostrar_menu()  #llamamos la funcion

# Ejecución del juego
jugar_ahorcado()    #llamamos la funcion principal
print("Trabajo hecho por Ulises Arguello")
