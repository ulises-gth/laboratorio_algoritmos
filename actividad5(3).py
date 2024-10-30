#ejercicio 1
# Crea una función llamada devolver_distintos() que reciba 3
# integers como parámetros.
# Si la suma de los 3 numeros es mayor a 15, va a devolver el
# número mayor.
# Si la suma de los 3 numeros es menor a 10, va a devolver el
# número menor.
# Si la suma de los 3 números es un valor entre 10 y 15
# (incluidos) va a devolver el número de valorintermedio.

def devolver_distintos(num1, num2, num3):
    suma = num1 + num2 + num3
    mayor = max(num1, num2, num3)
    menor = min(num1, num2, num3)
    intermedio = num1 + num2 + num3 - mayor - menor  
    if suma > 15:
        return mayor
    elif suma < 10:
        return menor
    else: 
        return intermedio
resultado = devolver_distintos(4, 7, 1)
print("Resultado:", resultado)


#Ejercicio 2
# Escribe una función (puedes ponerle cualquier nombre que
# quieras) que reciba cualquier palabra como parámetro, y que
# devuelva todas sus letras únicas (sin repetir) pero en orden
# alfabético.
# Por ejemplo si al invocar esta función pasamos la palabra
# "entretenido",deberia devolver ["d","e","i","n","o","r","t"]

def letras_unicas(palabra):

    letras = set(palabra) 
    letras_ordenadas = sorted(letras) 
    return letras_ordenadas
resultado = letras_unicas("entretenido")
print(resultado)
 

#ejercicio 3
# Escribe una función que requiera una cantidad indefinida de
# argumentos. Lo que hará esta función es devolver True si en
# algún momento se ha ingresado al numero cero repetido dos
# veces consecutivas.
# Por ejemplo:
# (5,6,1,0,0,9,3,5) >>> True
# (6,0,5,1,0,3,0,1) >>> False


def verificar_ceros_consecutivos(*args):
    for i in range(1, len(args)):
        if args[i] == 0 and args[i - 1] == 0:
            return True
    return False

resultado1 = verificar_ceros_consecutivos(5, 6, 1, 0, 0, 9, 3, 5)
resultado2 = verificar_ceros_consecutivos(6, 0, 5, 1, 0, 3, 0, 1)
print("Resultado 1:", resultado1) 
print("Resultado 2:", resultado2)  


#ejercicio 4
# Escribe una función llamada contar_primos() que requiera un
# solo argumento numérico.
# Esta función va a mostrar en pantalla todos los números
# primos existentes en el rango que va desde cero hasta ese
# número incluido, y va a devolver la cantidad de números
# primos que encontró.
# Aclaración, por convención el 0 y el 1 no se consideran primos.

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def contar_primos(n):
    cantidad_primos = 0
    print("Números primos en el rango de 0 a", n, ":")
    
    for num in range(2, n + 1): 
        if es_primo(num):
            print(num)
            cantidad_primos =cantidad_primos+1
    return cantidad_primos

resultado = contar_primos(20)
print("Cantidad de números primos encontrados:", resultado)

print("Trabajo hecho por Ulises Arguello")