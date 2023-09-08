import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)


def ejemplares_prestados():
    for libro in libros:
        if libro["cant_ej_pr"] > 0:
            print(f"Título: {libro['titulo']}\nEjemplares prestados: {libro['cant_ej_pr']}\n")
        else:
            print(f"Título: {libro['titulo']}\nNingún ejemplar prestado\n")


def registrar_nuevo_libro():
    # Ejecuto la funcion del modulo libro.py
    nuevo_libro = l.nuevo_libro()
    # Si la funcion retorna el libro se agrega a la lista
    if nuevo_libro != None:
        libros.append(nuevo_libro)


def eliminar_ejemplar_libro():
    codigo_libro = input("Ingrese código del libro: ")

    for i, libro in enumerate(libros):
        if libro.get("cod") == codigo_libro:
            encontrado = True
            indice_libro = i
            print("Libro encontrado.")
            break
        else:
            print("Libro inexistente.")

    if encontrado == True:
        ejemplares_disponibles = (libros[indice_libro]["cant_ej_ad"] - libros[indice_libro]["cant_ej_pr"])

        if ejemplares_disponibles > 0:
            confirmar_prestamo = input("¿Confirma la eliminación de un ejemplar de este libro? (Si/No) ")
            confirmar_prestamo = confirmar_prestamo.upper()

            if confirmar_prestamo == "SI":
                libros[indice_libro]["cant_ej_ad"] -= 1
                print("Ejemplar eliminado con éxito.")
            else:
                print("Eliminación de ejemplar cancelado.")


def prestar_ejemplar_libro():
    codigo_libro = input("Ingrese el código del libro: ")
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
        ejemplares_disponibles = (libros[indice_libro]["cant_ej_ad"] - libros[indice_libro]["cant_ej_pr"])

        print(f"""
              Título: {titulo }
              Autor: {autor}
              Ejemplares disponibles: {ejemplares_disponibles}
              """)

        if ejemplares_disponibles > 0:
            confirmar_prestamo = input("¿Confirma el préstamo de este libro? (Si/No) ")
            confirmar_prestamo = confirmar_prestamo.upper()

            if confirmar_prestamo == "SI":
                libros[indice_libro]["cant_ej_pr"] += 1
                print("Préstamo realizado con éxito.")
            else:
                print("Préstamo cancelado.")
        else:
            print("No quedan mas ejemplares disponibles.")
    else:
        print("Libro no encontrado")


def devolver_ejemplar_libro():
    codigo_libro = input("Ingrese el código del libro: ")
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
            ejemplares_disponibles = (libros[indice_libro]["cant_ej_ad"] - libros[indice_libro]["cant_ej_pr"])

            print(f"""
              Título: {titulo }
              Autor: {autor}
              Ejemplares disponibles: {ejemplares_disponibles}
              """)
            
            if libro["cant_ej_pr"] > 0:
                confirmar_devolucion = input("¿Confirma la devolución de este libro? (Si/No) ")
                confirmar_devolucion = confirmar_devolucion.upper()

                if confirmar_devolucion == "SI":
                    libros[indice_libro]["cant_ej_pr"] -= 1
                    print("Devolución realizada con éxito.")
                else:
                 print("Devolución cancelada.")
            else:
             print("Todos los ejemplares están disponible.")
    else:
     print("Libro no encontrado.")


def nuevo_libro():
    # completar
    return None
