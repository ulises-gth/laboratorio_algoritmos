nombre = input("Cual es tu nombre:")
print("Bueno",nombre,"he pensado un numero entre 1 y 100 y tienes solo ocho intentos para adivinar cual crees que es el numero")
contador=0
numero_intentos=8 

from random import randint
numero_ganador = randint(1,100)

while contador < numero_intentos:
    numerodel_usuario=int(input("Ingresa tu numero: "))
    if numerodel_usuario < 1 or numerodel_usuario > 100:
        print("El numero que debe ingresar debe estar entre 1 y 100: ")
    if numerodel_usuario != numero_ganador:
        print("Su numero es INCORRECTO")
    if numerodel_usuario < numero_ganador:
        print("El numero que penso es mayor a ese numero")
    if numerodel_usuario > numero_ganador:
        print("El numero que penso es menor a ese numero")
    contador=contador+1
    if numerodel_usuario == numero_ganador:
        print("Felicidades su numero es CORRECTO")    
        break
else:
    print("Perdiste, el numero que habia pensado", numero_ganador)

print("Este trabajo fue realizado por Ulises Arguello")