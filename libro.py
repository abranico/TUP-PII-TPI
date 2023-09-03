import cod_generator as cg

# Crear un diccionario para cada libro
libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}

def nuevo_libro():
    #Pido por consola los datos del nuevo libro
    codigo = generar_codigo()
    titulo = input("Ingrese el TITULO del libro: ")
    autor = input("Ingrese el AUTOR del libro: ")
    cant_ej_ad = int(input("Ingrese la cantidad de EJEMPLARES: "))
    #Creo el diccionario del nuevo libro con los datos ingresados
    nuevo_libro = {
        'cod': codigo,
        'cant_ej_ad': cant_ej_ad,
        'cant_ej_pr': 0,
        "titulo": titulo,
        "autor": autor
    }
    #Muestro el nuevo libro
    print(f"""
          Titulo: {titulo}
          Autor: {autor}
          Codigo: {codigo}
          Ejemplares: {cant_ej_ad}
          """)
    #Pido que el usuario confirme agregar el nuevo libro
    confirmacion = input("¿Esta seguro de añadir este libro? (Si/No): ")
    confirmacion = confirmacion.upper() # convierto a mayusculas
    #Valido para retornar el nuevo libro o no retornar nada.
    if confirmacion == "SI":
        print("Libro nuevo agregado.")
        return nuevo_libro
    else:
        print("Libro nuevo cancelado.")
    

def generar_codigo():
    codigo = cg.generar()
    return codigo


