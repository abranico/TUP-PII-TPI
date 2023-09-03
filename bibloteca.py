import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def ejemplares_prestados():
    # completar
    return None

def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    #completar
    return None

def eliminar_ejemplar_libro():
    #completar
    return None

def prestar_ejemplar_libro():
    codigo_libro = input("ingrese el codigo del libro: ")
    indice_libro = int()
    encontrado = False

    for i,libro in enumerate(libros):
        if libro.get('cod') == codigo_libro:
            indice_libro = i
            encontrado = True
            break
        
    if encontrado == True:
        titulo = libros[indice_libro]['titulo']
        autor = libros[indice_libro]['autor']
        ejemplares_disponibles = libros[indice_libro]['cant_ej_ad'] - libros[indice_libro]['cant_ej_pr']
        print(f"""
              Titulo: {titulo }
              Autor: {autor}
              Ejemplares disponibles: {ejemplares_disponibles}
              """)
        if ejemplares_disponibles > 0:
           confirmar_prestamo = input("¿Desea confirmar el prestamo de este libro? (Si/No) ")
           confirmar_prestamo = confirmar_prestamo.upper()
           if confirmar_prestamo == "SI":
               libros[indice_libro]['cant_ej_pr'] += 1
               print("Prestamo realizado con exito.")
           else:
               print("Prestamo cancelado.")
        else:
            print("No quedan mas ejemplares disponibles.")  
    else:
        print("Libro no encontrado")

def devolver_ejemplar_libro():
    #completar
    return None

def nuevo_libro():
    #completar
    return None