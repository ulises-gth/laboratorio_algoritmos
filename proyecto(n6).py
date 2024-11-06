import os
from pathlib import Path

# creamos la ruta base del programa(recetas)
ruta_base = Path.home() / "Recetas"

# Creamos la ruta base donde se guardan las recetas
BASE_DIR = Path.home() / 'Recetas'

# Lista de categorías
categorias = ['Carnes', 'Ensaladas', 'Postres', 'Pastas']

# Función para contar todas las recetas(en las categorias)
def contar_recetas():
    total_recetas = sum(len(files) for _, _, files in os.walk(BASE_DIR))
    return total_recetas

# Función para mostrar las categorías(disponibles)
def mostrar_categorias():
    categorias = []
    for folder in os.listdir(BASE_DIR):
        folder_path = BASE_DIR / folder
        if os.path.isdir(folder_path):
            categorias.append(folder)
    return categorias

# Función para mostrar recetas en una categoria(especifica)
def mostrar_recetas(categoria):
    categoria_path = BASE_DIR / categoria
    recetas = []
    for file in os.listdir(categoria_path):
        file_path = categoria_path / file
        if os.path.isfile(file_path):
            recetas.append(file)
    return recetas 

# Función para leer una receta
def leer_receta(categoria, receta):
    receta_path = BASE_DIR / categoria / receta
    file = open(receta_path, 'r', encoding='utf-8')
    contenido = file.read()
    print(contenido)
    file.close()

# Función para crear una nueva receta
def crear_receta(categoria, nombre_receta, contenido):
    receta_path = BASE_DIR / categoria / f"{nombre_receta}.txt"
    file = open(receta_path, 'w', encoding='utf-8')
    file.write(contenido)
    file.close()
    print(f"Receta '{nombre_receta}' creada exitosamente en la categoría '{categoria}'.")

# Función para crear una nueva categoría
def crear_categoria(nombre_categoria):
    nueva_categoria_path = BASE_DIR / nombre_categoria
    nueva_categoria_path.mkdir(exist_ok=True)
    print(f"Categoría '{nombre_categoria}' creada exitosamente.")

# Función para eliminar una receta
def eliminar_receta(categoria, receta):
    receta_path = BASE_DIR / categoria / receta
    receta_path.unlink()
    print(f"Receta '{receta}' eliminada exitosamente.")

# Función para eliminar una categoría
def eliminar_categoria(categoria):
    categoria_path = BASE_DIR / categoria
    for file in os.listdir(categoria_path):
        file_path = categoria_path / file
        if os.path.isfile(file_path):
            os.remove(file_path)
    os.rmdir(categoria_path)
    print(f"Categoría '{categoria}' eliminada exitosamente.")

#  Funcion para limpiar la consola
def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

# Función principal del menú
def menu():
    while True:
        limpiar_consola()
        print("Bienvenido al administrador de Recetas de U.Arguello")
        print("Ruta de recetas:", BASE_DIR)
        print("Total de recetas:", contar_recetas())
        print("\nElige una opción por favor: ")
        print("1- Leer receta")
        print("2- Crear receta nueva")
        print("3- Crear nueva categoría")
        print("4- Eliminar receta")
        print("5- Eliminar categoría")
        print("6- Salir")

        opcion = input("\nIngresa una opción: ")

        if opcion == '1':
            categorias = mostrar_categorias()
            print("\nCategorías disponibles:")
            for i in range(len(categorias)):
                print(f"{i + 1}. {categorias[i]}")
            cat_idx = int(input("\nElige una categoría: ")) - 1
            categoria = categorias[cat_idx]

            recetas = mostrar_recetas(categoria)
            print("\nRecetas disponibles:")
            for i in range(len(recetas)):
                print(f"{i + 1}. {recetas[i]}")
            rec_idx = int(input("\nElige una receta para leer: ")) - 1
            receta = recetas[rec_idx]

            print(f"\nLeyendo receta '{receta}':\n")
            leer_receta(categoria, receta)
            input("\nPresiona Enter para volver al menú...")

        elif opcion == '2':
            categorias = mostrar_categorias()
            print("\nCategorías disponibles:")
            for i in range(len(categorias)):
                print(f"{i + 1}. {categorias[i]}")
            cat_idx = int(input("\nElige una categoría: ")) - 1
            categoria = categorias[cat_idx]

            nombre_receta = input("Ingresa el nombre de la nueva receta: ")
            contenido_receta = input("Escribe el contenido de la receta:\n")

            crear_receta(categoria, nombre_receta, contenido_receta)
            input("\nPresiona Enter para volver al menú...")

        elif opcion == '3':
            nueva_categoria = input("Ingresa el nombre de la nueva categoría: ")
            crear_categoria(nueva_categoria)
            input("\nPresiona Enter para volver al menú...")

        elif opcion == '4':
            categorias = mostrar_categorias()
            print("\nCategorías disponibles:")
            for i in range(len(categorias)):
                print(f"{i + 1}. {categorias[i]}")
            cat_idx = int(input("\nElige una categoría: ")) - 1
            categoria = categorias[cat_idx]

            recetas = mostrar_recetas(categoria)
            print("\nRecetas disponibles:")
            for i in range(len(recetas)):
                print(f"{i + 1}. {recetas[i]}")
            rec_idx = int(input("\nElige una receta para eliminar: ")) - 1
            receta = recetas[rec_idx]

            eliminar_receta(categoria, receta)
            input("\nPresiona Enter para volver al menú...")

        elif opcion == '5':
            categorias = mostrar_categorias()
            print("\nCategorías disponibles:")
            for i in range(len(categorias)):
                print(f"{i + 1}. {categorias[i]}")
            cat_idx = int(input("\nElige una categoría para eliminar: ")) - 1
            categoria = categorias[cat_idx]

            eliminar_categoria(categoria)
            input("\nPresiona Enter para volver al menú...")

        elif opcion == '6':
            print("Finalizando programa, Adios que tengas buen dia :)")
            print("\nTrabajo hecho por Ulises Arguello")
            break
        
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            input("\nPresiona Enter para volver al menú...")

# Ejecutamos el menú atraves de llamar la funcion del menu(de opciones)
menu()
