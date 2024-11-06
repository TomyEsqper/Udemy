from os import system, remove
import os
from pathlib import Path


#En esta funcion Entro a la carpeta principal donde están las otras categorias del menú y lea cuales categorías hay con un ciclo for y las retorne
def lista_categorias():
    ruta =  Path(r'C:\Users\User\Documents\UDEMY\Dia 6\Recetas')
    categorias = [categoria.name for categoria in ruta.iterdir() if categoria.is_dir()]
    return categorias

#En esta funcion está establecido hasta la carpeta principar "Recetas"  y con f-string al final para leer la categoria elegida por el usuario en la 
#funcion "elegirOpcion", para luego leer la carpeta y mostrar todos los archvios txt

def recetas(categoriaInput):
    archivos  = Path(fr'C:\Users\User\Documents\UDEMY\Dia 6\Recetas\{categoriaInput}')

    for archivo in Path(archivos).glob("*.txt"):
        with open(archivo, 'r') as menus:
            print(menus.read())
#///////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////

#Esta funcion lo que hace es tomar las categorias de la carpeta "Receta" sacadas de la funcion lista_categorias y moostrar las opciones con un ciclo for
#En la parte de try saca el index de la opcion elegida por el usuario y con el if busca la carpeta por el index o por el nombre (len(categoraias))
#Y le devuelve a la funcion "recetas" el indice de la carpeta para que muestre los archivos ".txt" en esta categoría
def elegirOpcion():
    categorias = lista_categorias()
    opciones = '\n'.join([f"{i+1}. {categoria}" for i, categoria in enumerate(categorias)])
    categoriaInput = input(f"""
    Que categoría desea elegir....
    {opciones}
-> """).lower()
    
    try:
        categoriaIndex = int(categoriaInput) - 1
        if 0 <= categoriaIndex < len(categorias):
            recetas(categorias[categoriaIndex])
        else:
            print("Esta categoría no existe ")
    except ValueError:
        print("Esta Categoria no se encuentra en el menú.")
        
    
#Esta funcion lo que hace es tomar las categorias de la carpeta "Receta" sacadas de la funcion lista_categorias y moostrar las opciones con un ciclo for
#En la parte de try saca el index de la opcion elegida por el usuario y con el if busca la carpeta por el index o por el nombre (len(categoraias))
#Despeus de ubicar la carpeta pide, nombre y contendio del archivo ".txt" y lo agrega a la categoria seleccionada
def agregarReceta():
    categorias = lista_categorias()

    opciones = '\n'.join([f"{i+1}. {categoria}" for i, categoria in enumerate(categorias)])
    categoriaInput = input(f"""
    Que categoría desea elegir para cambiar agregar la reseta....
    {opciones}
-> """).lower()
    
    try:
        categoriaIndex = int(categoriaInput) - 1
        if 0 <= categoriaIndex < len(categorias):
            categoriaSeleccionada = categorias[categoriaIndex]
            rutaCategoria = Path(r'C:\Users\User\Documents\UDEMY\Dia 6\Recetas') / categoriaSeleccionada

            nombreRecetaNueva = input("\nIngrese el nombre de la nueva receta: ").capitalize() + ".txt" 
            ContenidoRecetaNueva = input("Ingrese ahora el contenido que desea que tenga su receta: \n")

            rutaArchivo = rutaCategoria  / nombreRecetaNueva

            with open(rutaArchivo, "w") as contenidoReceta:
                contenidoReceta.write(ContenidoRecetaNueva)

            print(f"Se ha agregado la receta {nombreRecetaNueva}, en la categoria {categoriaSeleccionada}")

    except ValueError:
        print("Opcion no valida. Intentelo de nuevo.")

#Esta funcion lo que hace es tomar las categorias de la carpeta "Receta" sacadas de la funcion lista_categorias y moostrar las opciones con un ciclo for
#Verifica si no existe ya esta carpeta, si no existe pide el nombre de la categoria y la crea en la carpeta "Recetas"
def crearCategoria():
    categoria = lista_categorias()

    categoriaACrear = input("Ingrese el nombre de la categoría: ").capitalize()
    try:
        if categoriaACrear not in categoria:
            rutaCategoriaNueva = Path(r'C:\Users\User\Documents\UDEMY\Dia 6\Recetas') / categoriaACrear
            rutaCategoriaNueva.mkdir()

            print(f"La categoría {categoriaACrear}, fue creada.")
        else:
            print("Esta categoria ya existe.")
    except ValueError:
        print("No se pudo crear la categoría.")

#Esta funcion lo que hace es tomar las categorias de la carpeta "Receta" sacadas de la funcion lista_categorias y moostrar las opciones con un ciclo for
#En la parte de try saca el index de la opcion elegida por el usuario y con el if busca la carpeta por el index o por el nombre (len(categoraias))
#Luego de esto muestra todos los nombre de los archivos ".txt" en la carpeta para elegir la que se desea eliminar con el comando "remove()"
def eliminarReceta():
    categorias = lista_categorias()
    opciones = '\n'.join([f"{i+1}. {categoria}" for i, categoria in enumerate(categorias)])
    categoriaInput = input(f"""
    Que categoría desea elegir....
    {opciones}
-> """).lower()
    
    try:
        categoriaIndex = int(categoriaInput)-1
        if 0 <= categoriaIndex < len(categorias):
            categoriaSeleccionada = categorias[categoriaIndex]
            rutaCategoria = Path(r'C:\Users\User\Documents\UDEMY\Dia 6\Recetas') / categoriaSeleccionada
            recetas = list(rutaCategoria.glob("*.txt"))

            if recetas:
                opcionesRecetas = '\n'.join([f"{i+1}. {receta.stem}" for i, receta in enumerate(recetas)])
                recetasInput = input(f"""
Elije la receta que deseas eliminar: 
{opcionesRecetas}
""").capitalize()
                try:
                    recetasIndex =  int(recetasInput) - 1
                    if 0 <= recetasIndex < len(recetas):
                        recetaSeleccionada = recetas[recetasIndex]
                        remove(recetaSeleccionada)

                        print(f"Se eliminó {recetaSeleccionada.stem}")
                    else:
                        print("Esta receta no exite")
                except ValueError:
                    print("No se puede hacer esto. Intente de nuevo.")
            else:
                print(f"No hay recetas en la categoria  {categoriaSeleccionada}")

        else:
            print("Categoria no encontrada")
    except ValueError:
        print("No se puede hacer esto. Intente de nuevo")
#Esta funcion lo que hace es tomar las categorias de la carpeta "Receta" sacadas de la funcion lista_categorias y moostrar las opciones con un ciclo for
#En la parte de try saca el index de la opcion elegida por el usuario y con el if busca la carpeta por el index o por el nombre (len(categoraias))
#Despues de ubicada la categoria la elimina con el comando "os.rmdir()"
def eliminarCategoria():
    categorias = lista_categorias()
    opciones = '\n'.join([f"{i+1}. {categoria}" for i, categoria in enumerate(categorias)])
    categoriaInput = input(f"""
    Que categoría desea elegir....
    {opciones}
-> """).lower()
    
    try:
        categoriaIndex = int(categoriaInput) - 1
        if 0 <= categoriaIndex < len(categorias):
            categoriaAEliminar = categorias[categoriaIndex]
            os.rmdir(fr'C:\Users\User\Documents\UDEMY\Dia 6\Recetas\{categoriaAEliminar}')
    except ValueError:
        print("Esta Categoria no se encuentra en el menú.")
#///////////////////////////////////////////////////////////////////////////////////////////////////

nombre = input("¡Bienvenido!, cual es tu Nombre: ")
while True:
    print(f"\nEsta bien {nombre}, elige una de estas 6 opciones.")
    opcion = int(input("""
        1. Opciones carta
        2. Agregar reseta
        3. Crear categoría Menú
        4. Eliminar reseta
        5. Eliminar categoría Menú
        6. Salir
    -> """))
    system('cls')
    match opcion:
        case 1:
            elegirOpcion()
        case 2:
            agregarReceta()
        case 3:
            crearCategoria()
        case 4:
            eliminarReceta()
        case 5:
            eliminarCategoria()
        case _:
            print("Saliendo del programa.")
            break

