import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)


def ejemplares_prestados():
    for  libro in libros:
        if libro["cant_ej_pr"]>0:
            print(f"Titulo: {libro['titulo']}\nEjemplares prestados: {libro['cant_ej_pr']}\n")
        else:
            print(f"Titulo: {libro['titulo']}\nNingun ejemplar prestado\n")

        
    return None


def registrar_nuevo_libro():
    # Ejecuto la funcion del modulo libro.py
    nuevo_libro = l.nuevo_libro()
    # Si la funcion retorna el libro se agrega a la lista
    if nuevo_libro != None:
        libros.append(nuevo_libro)


def eliminar_ejemplar_libro():
    codigo_libro = input("Ingrese codigo del libro: ")
    for i, libro in enumerate(libros):
        if libro.get('cod') == codigo_libro:
            encontrado = True
            indice_libro = i
            print("Libro encontrado.")
            break
        else:
            print("Libro inexistente.")
    if encontrado == True:
        ejemplares_disponibles = (
            libros[indice_libro]["cant_ej_ad"] - libros[indice_libro]["cant_ej_pr"]
        )
        if ejemplares_disponibles > 0:
            confirmar_prestamo = input(
                "¿Desea confirmar la eliminacion de 1 ejemplar de este libro? (Si/No) "
            )
            confirmar_prestamo = confirmar_prestamo.upper()
            if confirmar_prestamo == "SI":
                libros[indice_libro]["cant_ej_ad"] -= 1
                print("Ejemplar eliminado con exito.")
            else:
                print("Eliminacion de ejemplar cancelado.")


    return None


def prestar_ejemplar_libro():
    codigo_libro = input("ingrese el codigo del libro: ")
    indice_libro = int()
    encontrado = False

    for i, libro in enumerate(libros):
        if libro.get("cod") == codigo_libro:
            indice_libro = i
            encontrado = True
            break

    if encontrado == True:
        titulo = libros[indice_libro]["titulo"]
        autor = libros[indice_libro]["autor"]
        ejemplares_disponibles = (
            libros[indice_libro]["cant_ej_ad"] - libros[indice_libro]["cant_ej_pr"]
        )
        print(
            f"""
              Titulo: {titulo }
              Autor: {autor}
              Ejemplares disponibles: {ejemplares_disponibles}
              """
        )
        if ejemplares_disponibles > 0:
            confirmar_prestamo = input(
                "¿Desea confirmar el prestamo de este libro? (Si/No) "
            )
            confirmar_prestamo = confirmar_prestamo.upper()
            if confirmar_prestamo == "SI":
                libros[indice_libro]["cant_ej_pr"] += 1
                print("Prestamo realizado con exito.")
            else:
                print("Prestamo cancelado.")
        else:
            print("No quedan mas ejemplares disponibles.")
    else:
        print("Libro no encontrado")


def devolver_ejemplar_libro():
    # completar
    return None


def nuevo_libro():
    # completar
    return None
