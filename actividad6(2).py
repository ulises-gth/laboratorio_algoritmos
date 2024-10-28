import os
from pathlib import Path, PureWindowsPath

# ruta = os.getcwd()

# print("la ruta actual es : ", ruta)

# carpeta = Path('C:/Users/marco/OneDrive/Escritorio/terciario') 

# ruta_windows = PureWindowsPath(carpeta)

# ruta = os.chdir('C:/Users/marco/OneDrive/Escritorio/terciario') #cambiar directorio  

# ruta = os.mkdir('C:/Users/marco/OneDrive/Escritorio/terciario/NuevaCarpeta') #crear directorio 

# ruta = os.rmdir('C:/Users/marco/OneDrive/Escritorio/terciario/NuevaCarpeta') #eliminar directorio

# ruta = os.mkdir('C:/Users/marco/OneDrive/Escritorio/terciario/NuevaCarpeta') #crear directorio 




# carpeta = Path('C:/Users/marco/OneDrive/Escritorio/terciario/pythonCurso') / 'registro.txt'

# print(carpeta.read_text())
# print(carpeta.name)

# print(carpeta.suffix)

# if not carpeta.exists():
#     print("Este archivo no existe")
# else: 
#     print("Genial, existe ")

# base = Path.home()
# guia = Path(base, "Europa","España",Path("Barcelona", "Sagrada familia.txt"))

# print(guia.parent)

# print(guia.parent.parent)

# guia = Path(Path.home(),"Europa")

# for txt in Path(guia).glob("*.txt"): #todos los archivos del directorio europa
#     print(txt)


# for txt in Path(guia).glob("**/*.txt"): #todos los archivos del directorio europa mas las sub carpetas
#     print(txt)

# guia = Path("Europa", "España", "Barcelona","SagradaFamilia.txt")

# en_europa = guia.relative_to("Europa")
# en_espania = guia.relative_to("Europa","España")
# print(en_europa)
# print(en_espania)


# Práctica Path 1
# Almacena en la variable ruta_base, un objeto Path que señale el directorio base del usuario.
# Recuerda importar Path del módulo pathlib, y utilizar el método home()

ruta_base=Path.home()
print("Directorio base del usuario:", ruta_base)


# Práctica Path 2
# Implementa y crea una ruta relativa que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:
# "Curso Python"
# "Día 6"
# "practicas_path.py"
# Almacena el directorio obtenido en la variable ruta. No olvides importar Path

ruta_relativa=Path("Curso Phyton", "Dia 6", "practicas_path.py")
print("Ruta relativa:", ruta_relativa)


# Práctica Path 3
# Implementa y crea una ruta absoluta que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:
# Almacena el directorio obtenido en la variable ruta. No olvides importar Path, y de concatenar el objeto Path que refiere a la carpeta base del usuario

ruta_absoluta=Path(Path.home(),"Curso Phyton","Dia 6", "practicas_path.py")
print("Ruta absoluta:",ruta_absoluta)


# from os import system

# nombre = input("Dime tu numbre : ")

# edad = input("Dime tu edad : ")

# system('cls')

# print(nombre)
# print(edad)


# Práctica Archivos y Funciones 1
# Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, 
# y devuelva su contenido (read).

def abrir_leer(archivo):
    file=open(archivo,"r")
    contenido=file.read()
    file.close()
    return contenido

# Práctica Archivos y Funciones 2
# Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro, 
# y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"

def sobrescribir(archivo):
    file=open(archivo,"w")
    file.write("contenido eliminado")
    file.close()

# Práctica Archivos y Funciones 3
# Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro, y 
# lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución". 
# Finalmente, debe cerrar el archivo abierto.

def registro_error(archivo):
    file=open(archivo,"a")
    file.write("\nSe ha registrado un error de ejecucion")
    file.close()

print("Trabajo hecho por Ulises Arguello")